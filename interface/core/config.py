import os, sys
from dotenv import load_dotenv

load_dotenv()

DEFAULT_LLM_API_KEY = os.getenv("GEMINI_API_KEY")
import os
from dotenv import load_dotenv

load_dotenv()  # Load .env file if exists

DEFAULT_PROVIDER = os.getenv("LLM_PROVIDER", "gemini")
DEFAULT_MODEL = os.getenv("LLM_MODEL", "gemini-1.5-flash")
