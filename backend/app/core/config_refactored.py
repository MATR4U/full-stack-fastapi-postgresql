import secrets
import warnings
from typing import Annotated, Any, Literal

from pydantic import (
    AnyUrl,
    BeforeValidator,
    HttpUrl,
    PostgresDsn,
    computed_field,
    model_validator,
)
from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing_extensions import Self


def parse_cors(v: Any) -> list[str] | str:
    if isinstance(v, str) and not v.startswith("["):
        return [i.strip() for i in v.split(",")]
    elif isinstance(v, list | str):
        return v
    raise ValueError(v)


class DatabaseSettings(BaseSettings):

    POSTGRES_SERVER: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str = "user"
    POSTGRES_PASSWORD: str = "password"
    POSTGRES_DB: str = "dbname"

    @computed_field  # type: ignore[misc]
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> PostgresDsn:
        return MultiHostUrl.build(
            scheme="postgresql+psycopg",
            username=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_SERVER,
            port=self.POSTGRES_PORT,
            path=f"/{self.POSTGRES_DB}",
        )
    


    





class EmailSettings(BaseSettings):
    project_name: str | None = None
    SMTP_TLS: bool = True
    SMTP_SSL: bool = False
    SMTP_PORT: int = 587
    SMTP_HOST: str | None = None
    SMTP_USER: str | None = None
    SMTP_PASSWORD: str | None = None
    EMAILS_FROM_EMAIL: str | None = None
    EMAILS_FROM_NAME: str | None = None
    EMAIL_RESET_TOKEN_EXPIRE_HOURS: int = 48
    EMAIL_TEST_USER: str = "test@example.com"

    @model_validator(mode="after")
    def _set_default_emails_from(self) -> Self:
if not self.EMAILS_FROM_NAME:
    self.EMAILS_FROM_NAME = self.project_name
        return self

    @computed_field  # type: ignore[misc]
    @property
    def emails_enabled(self) -> bool:
        return bool(self.SMTP_HOST and self.EMAILS_FROM_EMAIL)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_ignore_empty=True, extra="ignore"
    )
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    DOMAIN: str = "localhost"
    ENVIRONMENT: Literal["local", "staging", "production"] = "local"
    BACKEND_CORS_ORIGINS: Annotated[
        list[AnyUrl] | str, BeforeValidator(parse_cors)
    ] = []
    PROJECT_NAME: str = "My Project"
    SENTRY_DSN: HttpUrl | None = None
    FIRST_SUPERUSER: str = "admin"
    FIRST_SUPERUSER_PASSWORD: str = "adminpassword"
    USERS_OPEN_REGISTRATION: bool = False

    database: DatabaseSettings = DatabaseSettings(
        POSTGRES_SERVER="localhost",
        POSTGRES_USER="user",
        POSTGRES_PASSWORD="password",
        POSTGRES_DB="dbname"
    )
    email: EmailSettings = EmailSettings(
EMAILS_FROM_NAME="My Project", project_name="My Project",
        EMAILS_FROM_EMAIL="noreply@myproject.com"
    )

    @computed_field  # type: ignore[misc]
    @property
    def server_host(self) -> str:
        if self.ENVIRONMENT == "local":
            return f"http://{self.DOMAIN}"
        return f"https://{self.DOMAIN}"

    def _check_default_secret(self, var_name: str, value: str | None) -> None:
        if value == "changethis":
            warnings.warn(
                f"The {var_name} is set to the default value. "
                "Please change it to a more secure value.",
                UserWarning,
            )
    model_config = SettingsConfigDict(
        env_file=".env", env_ignore_empty=True, extra="ignore"
    )
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    DOMAIN: str = "localhost"
    ENVIRONMENT: Literal["local", "staging", "production"] = "local"
    BACKEND_CORS_ORIGINS: Annotated[
        list[AnyUrl] | str, BeforeValidator(parse_cors)
    ] = []
    PROJECT_NAME: str
    SENTRY_DSN: HttpUrl | None = None
    FIRST_SUPERUSER: str
    FIRST_SUPERUSER_PASSWORD: str
    USERS_OPEN_REGISTRATION: bool = False

    database: DatabaseSettings = DatabaseSettings()
    email: EmailSettings = EmailSettings()

    @computed_field  # type: ignore[misc]
    @property
    def server_host(self) -> str:
        if self.ENVIRONMENT == "local":
            return f"http://{self.DOMAIN}"
        return f"https://{self.DOMAIN}"

    def _check_default_secret(self, var_name: str, value: str | None) -> None:
        if value == "changethis":
            warnings.warn(
                f"The {var_name} is set to the default value. "
                "Please change it to a more secure value.",
                UserWarning,
            )
