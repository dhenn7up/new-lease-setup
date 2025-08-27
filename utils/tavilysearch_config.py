import os
from pathlib import Path
from dotenv import load_dotenv


def get_tavily_config():
    # Get the root directory of the project (adjust if needed)
    BASE_DIR = Path(__file__).resolve().parent.parent

    # Load environment variables from `.env`
    load_dotenv(BASE_DIR / 'venv' / '.env')

    config = {
        "api_key": os.getenv("TAVILY_API_KEY"),
    }

    # Optionally validate required keys
    missing_keys = [k for k, v in config.items() if not v]
    if missing_keys:
        raise ValueError(f"Missing environment variables: {', '.join(missing_keys)}")

    return config
