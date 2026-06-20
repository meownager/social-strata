from pathlib import Path


SCHEMA = Path("data/schema.sql").read_text(encoding="utf-8")


def test_generated_outputs_schema_matches_phase_one_row() -> None:
    expected_columns = [
        "product_category TEXT NOT NULL",
        "visible_attributes JSONB",
        "style_notes TEXT",
        "likely_use_case TEXT",
        "confidence TEXT",
        "audience TEXT",
        "buyer_intent TEXT",
        "caption_angle TEXT",
        "tone TEXT",
        "hashtag_themes JSONB",
        "campaign_style TEXT",
        "event_details JSONB",
        "caption TEXT NOT NULL",
        "hashtags JSONB NOT NULL",
        "social_media_post TEXT NOT NULL",
    ]

    assert "CREATE TABLE IF NOT EXISTS generated_outputs" in SCHEMA
    for column in expected_columns:
        assert column in SCHEMA


def test_schema_keeps_future_learning_tables() -> None:
    assert "CREATE TABLE IF NOT EXISTS user_feedback" in SCHEMA
    assert "CREATE TABLE IF NOT EXISTS instagram_metrics" in SCHEMA
    assert "generated_output_id UUID REFERENCES generated_outputs(id)" in SCHEMA
