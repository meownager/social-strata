from src.config import AppConfig
from src.database import SupabaseDatabase, build_generated_output_row
from src.relevance_engine import (
    EventDetails,
    build_relevance_profile,
    format_social_media_post,
    generate_output,
    identify_product_context,
)


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
