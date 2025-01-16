import os

from pydantic import Field, PostgresDsn, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppConfig(BaseSettings):
    process_id: int = Field(default_factory=lambda: os.getpid())


class DatabaseConfig(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="pg_")

    user: str = Field(default="postgres")
    password: str = Field(default="postgres")
    host: str = Field(default="postgres")
    port: str = Field(default="5432")
    dbname: str = Field(default="mydb")

    @computed_field  # type: ignore[prop-decorator]
    @property
    def POSTGRES_URI(self) -> PostgresDsn:
        return PostgresDsn.build(
            scheme="postgresql+psycopg2",
            username=self.user,
            password=self.password,
            host=self.host,
            port=int(self.port),
            path=self.dbname,
        )
