from src.config import AppConfig
from src.database import SupabaseDatabase, build_generated_output_row
from src.relevance_engine import (
    EventDetails,
    build_relevance_profile,
    format_social_media_post,
    generate_output,
    identify_product_context,
)


class FakeQuery:
    def __init__(self, data: list[dict[str, str]] | None = None, error: Exception | None = None) -> None:
        self.data = data or []
        self.error = error

    def select(self, _columns: str) -> "FakeQuery":
        return self

    def limit(self, _count: int) -> "FakeQuery":
        return self

    def execute(self) -> object:
        if self.error is not None:
            raise self.error
        return type("Response", (), {"data": self.data})()


class FakeClient:
    def __init__(self, query: FakeQuery) -> None:
        self.query = query
        self.table_name = ""

    def table(self, name: str) -> FakeQuery:
        self.table_name = name
        return self.query


def test_generated_output_row_contains_phase_one_data() -> None:
    context = identify_product_context(
        filename="modal-hijab.jpg",
        image_size=(900, 1200),
        product_note="modal hijab summer",
    )
    profile = build_relevance_profile(context)
    output = generate_output(context, profile, campaign_style="Summer staple")
    post = format_social_media_post(output.caption, output.hashtags)
    event_details = EventDetails(location="Al-Huda, Fishers", dates="June 19 and 26")

    row = build_generated_output_row(
        context=context,
        profile=profile,
        output=output,
        campaign_style="Summer staple",
        event_details=event_details,
        social_media_post=post,
    )

    assert row["product_category"] == "hijab"
    assert row["campaign_style"] == "Summer staple"
    assert row["event_details"]["location"] == "Al-Huda, Fishers"
    assert row["hashtags"] == output.hashtags
    assert row["social_media_post"] == post


def test_database_skips_save_without_supabase_config() -> None:
    database = SupabaseDatabase(AppConfig())

    result = database.save_generated_output({"caption": "test"})

    assert not result.saved
    assert result.reason == "Supabase is not configured."


def test_database_connection_check_skips_without_supabase_config() -> None:
    database = SupabaseDatabase(AppConfig())

    result = database.check_connection()

    assert not result.connected
    assert result.reason == "Supabase is not configured."


def test_database_connection_check_uses_generated_outputs_table() -> None:
    client = FakeClient(FakeQuery())
    database = SupabaseDatabase(
        AppConfig(supabase_url="https://example.supabase.co", supabase_key="anon-key"),
        client=client,
    )

    result = database.check_connection()

    assert result.connected
    assert result.reason == "Supabase is connected."
    assert client.table_name == "generated_outputs"


def test_database_connection_check_reports_failures() -> None:
    client = FakeClient(FakeQuery(error=RuntimeError("table missing")))
    database = SupabaseDatabase(
        AppConfig(supabase_url="https://example.supabase.co", supabase_key="anon-key"),
        client=client,
    )

    result = database.check_connection()

    assert not result.connected
    assert "table missing" in result.reason
