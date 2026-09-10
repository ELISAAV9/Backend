import os


class Config:
    DATABASE_PATH = os.getenv("DATABASE_PATH", "bank.db")

    BANK_ENCRYPTION_KEY = os.getenv("BANK_ENCRYPTION_KEY")
    if not BANK_ENCRYPTION_KEY:
        raise RuntimeError(
            "BANK_ENCRYPTION_KEY environment variable is required"
        )

    API_SECRET = os.getenv("API_SECRET")
    if not API_SECRET:
        raise RuntimeError(
            "API_SECRET environment variable is required"
        )