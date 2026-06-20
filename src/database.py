"""Supabase database adapter for Social-Strata.

The adapter is safe to import and test without real credentials. When Supabase
configuration is missing, save calls return a skipped result instead of failing.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from supabase import Client, create_client

try:
    from .config import AppConfig
    from .relevance_engine import EventDetails, GeneratedOutput, ProductContext, RelevanceProfile
except ImportError:
    from config import AppConfig
    from relevance_engine import EventDetails, GeneratedOutput, ProductContext, RelevanceProfile


@dataclass(frozen=True)
class SaveResult:
    saved: bool
    reason: str
    output_id: str | None = None


@dataclass(frozen=True)
class ConnectionStatus:
    connected: bool
    reason: str


def build_generated_output_row(
    context: ProductContext,
    profile: RelevanceProfile,
    output: GeneratedOutput,
    campaign_style: str,
    event_details: EventDetails,
    social_media_post: str,
) -> dict[str, Any]:
    """Build the row shape used by the Phase 1 generated_outputs table."""
    return {
        "product_category": context.product_category,
        "visible_attributes": context.visible_attributes,
        "style_notes": context.style_notes,
        "likely_use_case": context.likely_use_case,
        "confidence": context.confidence,
        "audience": profile.audience,
        "buyer_intent": profile.buyer_intent,
        "caption_angle": profile.caption_angle,
        "tone": profile.tone,
        "hashtag_themes": profile.hashtag_themes,
        "campaign_style": campaign_style,
        "event_details": {
            "location": event_details.location,
            "dates": event_details.dates,
            "time": event_details.time,
            "closing_line": event_details.closing_line,
        },
        "caption": output.caption,
        "hashtags": output.hashtags,
        "social_media_post": social_media_post,
    }


class SupabaseDatabase:
    def __init__(self, config: AppConfig, client: Client | None = None) -> None:
        self.config = config
        self.client = client

    def is_configured(self) -> bool:
        return self.config.has_supabase

    def _client(self) -> Client:
        if self.client is not None:
            return self.client
        if not self.config.has_supabase:
            raise RuntimeError("Supabase is not configured.")
        self.client = create_client(self.config.supabase_url, self.config.supabase_key)
        return self.client

    def save_generated_output(self, row: dict[str, Any]) -> SaveResult:
        if not self.config.has_supabase:
            return SaveResult(saved=False, reason="Supabase is not configured.")

        response = self._client().table("generated_outputs").insert(row).execute()
        data = response.data or []
        output_id = data[0].get("id") if data else None
        return SaveResult(saved=True, reason="Saved generated output.", output_id=output_id)

    def check_connection(self) -> ConnectionStatus:
        if not self.config.has_supabase:
            return ConnectionStatus(connected=False, reason="Supabase is not configured.")

        try:
            self._client().table("generated_outputs").select("id").limit(1).execute()
        except Exception as exc:
            return ConnectionStatus(connected=False, reason=f"Supabase connection failed: {exc}")

        return ConnectionStatus(connected=True, reason="Supabase is connected.")
