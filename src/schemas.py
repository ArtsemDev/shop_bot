from pydantic import BaseSettings, PostgresDsn, SecretStr


class Settings(BaseSettings):
    DATABASE_URL: PostgresDsn
    BOT_TOKEN: SecretStr
