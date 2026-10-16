"""Static fake-credential fixture for Sentinel V2. This file is never executed."""

# SYNTHETIC ONLY — not a credential; do not authenticate with this value.
from openai import OpenAI

OPENAI_API_KEY: str = "SENTINEL_FAKE_OPENAI_DO_NOT_USE_7vK3pQ9mN2xR6aB4cD8eF1gH5jL0s"
client = OpenAI(api_key=OPENAI_API_KEY)
