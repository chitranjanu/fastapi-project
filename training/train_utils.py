from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

APP_DIR = BASE_DIR / "app"

# Prevent accidentally creating another app folder.
if not APP_DIR.is_dir():
    raise FileNotFoundError(f"Original app folder not found: {APP_DIR}")

DATA_DIR = BASE_DIR / "data"
DATA_FILE_NAME = "car-details.csv"
DATA_FILE_PATH = DATA_DIR / DATA_FILE_NAME

MODEL_DIR_NAME = "models"
MODEL_NAME = "model.joblib"

MODEL_DIR = APP_DIR / MODEL_DIR_NAME
MODEL_PATH = MODEL_DIR / MODEL_NAME
