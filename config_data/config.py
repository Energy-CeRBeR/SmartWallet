from dataclasses import dataclass
from pathlib import Path

from environs import Env
from pydantic import BaseModel
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).parent.parent


@dataclass
class DataBase:
    URL: str


class AuthJWT(BaseModel):
    private_key_path: Path = BASE_DIR / "auth_upd" / "certs" / "jwt-private.pem"
    public_key_path: Path = BASE_DIR / "auth_upd" / "certs" / "jwt-public.pem"
    algorithm: str = "RS256"
    access_token_expire_minutes: int = 15


@dataclass
class Config:
    database: DataBase


class Settings(BaseSettings):
    auth_jwt: AuthJWT = AuthJWT()


settings = Settings()


def load_config(path: str | None = None) -> Config:
    env: Env = Env()
    env.read_env(path)

    return Config(database=DataBase(URL=env('DATABASE_URL')))
