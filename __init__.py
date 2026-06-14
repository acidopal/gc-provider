"""Hermes plugin shim for the GrowthCircle.id model provider.

This repository is primarily an OpenClaw provider plugin.  Hermes discovers
model providers from Python ``ProviderProfile`` objects, so this small shim lets
one Git repo install cleanly into both OpenClaw and Hermes:

    hermes plugins install Growth-Circle/gc-provider --enable

The provider is OpenAI-compatible at https://ai.growthcircle.id/v1 and uses the
GROWTHCIRCLE_API_KEY environment variable.
"""

from __future__ import annotations

from providers import register_provider
from providers.base import ProviderProfile

BASE_URL = "https://ai.growthcircle.id/v1"
ENV_VAR = "GROWTHCIRCLE_API_KEY"

FREE_TEXT_MODELS = (
    "gpt-5.3-codex-free",
    "gpt-5.4-free",
    "gpt-5.4-mini-free",
    "gpt-5.5-free",
    "claude-haiku-4-5-20251001-free",
    "claude-opus-4-6-free",
    "claude-opus-4-7-free",
    "claude-sonnet-4-6-free",
    "deepseek-v4-flash-free",
    "deepseek-v4-pro-free",
    "gemini-2.5-flash-free",
    "gemini-2.5-flash-lite-free",
    "gemini-2.5-pro-free",
    "gemini-3-flash-preview-free",
    "gemini-3-pro-preview-free",
    "gemini-3.1-pro-preview-free",
    "MiniMax-M2.7-free",
    "MiniMax-M3-free",
    "MiniMax-M2.7-highspeed-free",
)

PAID_TEXT_MODELS = (
    "gpt-5.3-codex",
    "gpt-5.3-codex-spark",
    "gpt-5.4",
    "gpt-5.4-mini",
    "gpt-5.5",
    "claude-3-5-haiku-latest",
    "claude-haiku-4-5-20251001",
    "claude-haiku-4-5-20251001-thinking",
    "claude-opus-4-5-20251101",
    "claude-opus-4-5-20251101-thinking",
    "claude-opus-4-6",
    "claude-opus-4-6-thinking",
    "claude-opus-4-7",
    "claude-sonnet-4-5-20250929",
    "claude-sonnet-4-5-20250929-thinking",
    "claude-sonnet-4-6",
    "claude-sonnet-4-6-thinking",
    "deepseek-r1-0528",
    "deepseek-v3.2",
    "deepseek-v4-flash",
    "deepseek-v4-pro",
    "gemini-2.5-flash",
    "gemini-2.5-flash-lite",
    "gemini-2.5-pro",
    "gemini-3-flash-preview",
    "gemini-3-pro-preview",
    "gemini-3.1-pro-preview",
    "glm-4.6",
    "glm-4.7",
    "glm-5",
    "glm-5.1",
    "kimi-k2-instruct",
    "kimi-k2-thinking",
    "kimi-k2.5",
    "MiniMax-M2.7",
    "MiniMax-M3",
    "MiniMax-M2.7-highspeed",
)

TEAM_TEXT_MODELS = (
    "gpt-5.3-codex",
    "gpt-5.3-codex-spark",
    "gpt-5.4",
    "gpt-5.4-mini",
    "gpt-5.5",
)

# Fallback catalog used by `hermes setup model` / `hermes model` when the live
# /v1/models request cannot be fetched yet (for example before a key is saved).
FALLBACK_MODELS = tuple(dict.fromkeys((*TEAM_TEXT_MODELS, *PAID_TEXT_MODELS, *FREE_TEXT_MODELS)))


growthcircle = ProviderProfile(
    name="growthcircle",
    aliases=("gc", "growthcircle-id", "growthcircle.id"),
    display_name="GrowthCircle.id",
    description="GrowthCircle.id — OpenAI-compatible text and vision models",
    signup_url="https://growthcircle.id/app/ai",
    env_vars=(ENV_VAR, "GROWTHCIRCLE_BASE_URL"),
    base_url=BASE_URL,
    models_url=f"{BASE_URL}/models",
    auth_type="api_key",
    supports_vision=True,
    fallback_models=FALLBACK_MODELS,
    default_aux_model="gpt-5.5-free",
)

register_provider(growthcircle)


# General Hermes plugin loader calls register(ctx) for standalone plugins.
# ProviderProfile registration already happens at import time above; this no-op
# keeps `hermes plugins list` clean if the plugin is explicitly enabled.
def register(ctx):
    return None
