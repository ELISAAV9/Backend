from fastapi import Header, HTTPException

from app.config import Config


def verify_api_key(x_api_key: str | None = Header(default=None)):
    if x_api_key != Config.API_SECRET:
        raise HTTPException(
            status_code=401,
            detail="Invalid API key",
        )

    return True