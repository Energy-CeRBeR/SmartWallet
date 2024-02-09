from dataclasses import dataclass
from environs import Env


@dataclass
class DataBase:
    URL: str


@dataclass
class Config:
    database: DataBase


def load_config(path: str | None = None) -> Config:
    env: Env = Env()
    env.read_env(path)

    return Config(database=DataBase(URL=env('DATABASE_URL')))
