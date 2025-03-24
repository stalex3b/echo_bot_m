from dataclasses import dataclass
from environs import Env
from pathlib import Path

@dataclass
class TgBot:
    token: str  # Токен для доступа к телеграм-боту

@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: Path | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBot(token=env('BOT_TOKEN')))
