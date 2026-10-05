from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8'
    )

    DATABASE_URL: str = 'sqlite:///database.db'
    # ECHO_SQL: bool = False
    # SECRET_KEY: str  # obrigatório, sem default


settings = Settings()
