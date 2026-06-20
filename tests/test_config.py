from src.config import AppConfig


def test_config_flags_are_false_without_secrets() -> None:
    config = AppConfig()

    assert not config.has_supabase
    assert not config.has_gemini


def test_config_flags_detect_available_services() -> None:
    config = AppConfig(
        supabase_url="https://example.supabase.co",
        supabase_key="anon-key",
        gemini_api_key="gemini-key",
    )

    assert config.has_supabase
    assert config.has_gemini
