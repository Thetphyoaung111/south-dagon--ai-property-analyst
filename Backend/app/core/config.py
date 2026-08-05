from pathlib import Path

# Backend folder
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Project root (SouthdagonAI)
PROJECT_ROOT = BASE_DIR.parent

DATABASE_URL = f"sqlite:///{BASE_DIR}/south_dagon_ai.db"

DATASET_FILE = PROJECT_ROOT / "Datasets" / "south_dagon_properties.csv"