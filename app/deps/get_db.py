from typing import Generator
from fastapi.security import OAuth2PasswordBearer

from app.db.session import SessionLocal
from app.core.config import settings


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
