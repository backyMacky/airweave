"""Auth config."""

from pydantic import Field

from app.platform.configs._base import BaseConfig


class AuthConfig(BaseConfig):
    """Authentication config schema."""

    pass


class APIKeyAuthConfig(AuthConfig):
    """API key authentication credentials schema."""

    api_key: str = Field(title="API Key", description="The API key for the API")


class OpenAIAuthConfig(APIKeyAuthConfig):
    """OpenAI authentication credentials schema."""

    api_key: str = Field(title="API Key", description="The API key for the OpenAI account")


class URLAndAPIKeyAuthConfig(AuthConfig):
    """URL and API key authentication credentials schema."""

    url: str = Field(title="URL", description="The URL of the API")
    api_key: str = Field(title="API Key", description="The API key for the API")


class WeaviateAuthConfig(AuthConfig):
    """Weaviate authentication credentials schema."""

    cluster_url: str = Field(title="Cluster URL", description="The URL of the Weaviate cluster")
    api_key: str = Field(title="API Key", description="The API key for the Weaviate cluster")


class ODBCAuthConfig(AuthConfig):
    """ODBC authentication credentials schema."""

    host: str = Field(title="Host", description="The host of the ODBC database")
    port: int = Field(title="Port", description="The port of the ODBC database")
    database: str = Field(title="Database", description="The name of the ODBC database")
    username: str = Field(title="Username", description="The username for the ODBC database")
    password: str = Field(title="Password", description="The password for the ODBC database")


class StripeAuthConfig(AuthConfig):
    """Stripe authentication credentials schema."""

    api_key: str = Field(title="API Key", description="The API key for the Stripe account")


class PostgreSQLAuthConfig(BaseConfig):
    """PostgreSQL authentication configuration."""

    host: str = Field(title="Host", description="The host of the PostgreSQL database")
    port: int = Field(title="Port", description="The port of the PostgreSQL database")
    database: str = Field(title="Database", description="The name of the PostgreSQL database")
    user: str = Field(title="Username", description="The username for the PostgreSQL database")
    password: str = Field(title="Password", description="The password for the PostgreSQL database")
    schema: str = Field(
        default="public",
        title="Schema",
        description="The schema of the PostgreSQL database",
    )
    tables: str = Field(
        default="*",
        title="Tables",
        description=(
            "Comma separated list of tables to sync. For example, 'users,orders'. "
            "For all tables, use '*'"
        ),
    )

    class Config:
        """Pydantic config."""

        json_schema_extra = {
            "example": {
                "host": "localhost",
                "port": 5432,
                "database": "mydb",
                "user": "postgres",
                "password": "secret",
                "schema": "public",
                "tables": "users,orders",
            }
        }
