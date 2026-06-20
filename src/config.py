"""Environment configuration for Social-Strata.

Secrets should come from a local `.env` file during development or from cloud
secrets in deployment. They should never be committed to GitHub.
"""

from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass(frozen=True)
class AppConfig:
    supabase_url: str = ""
    supabase_key: str = ""
    gemini_api_key: str = ""

    @property
    def has_supabase(self) -> bool:
        return bool(self.supabase_url and self.supabase_key)

    @property
    def has_gemini(self) -> bool:
        return bool(self.gemini_api_key)


def load_config() -> AppConfig:
    """Load app configuration from environment variables."""
    load_dotenv()
    return AppConfig(
        supabase_url=os.getenv("SUPABASE_URL", "").strip(),
        supabase_key=os.getenv("SUPABASE_KEY", "").strip(),
        gemini_api_key=os.getenv("GEMINI_API_KEY", "").strip(),
    )
