import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "development-key")
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
    AUTOSAVE_DELAY = int(os.getenv("AUTOSAVE_DELAY", "2000"))
