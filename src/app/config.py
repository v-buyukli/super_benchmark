from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


load_dotenv()


class Settings(BaseSettings):
    DEBUG: bool = Field(default=True, validation_alias='SUPERBENCHMARK_DEBUG')
    HOST: str = Field(default='127.0.0.1')
    PORT: int = Field(default=8000)

    model_config = SettingsConfigDict(env_file='.env')


settings = Settings()
