import pydantic

__all__ = ("api_settings", "mongo_settings", "jwt_settings",)


class BaseSettings(pydantic.BaseSettings):
    class Config:
        env_file = ".env"


class APISettings(BaseSettings):
    title: str = "People API"
    host: str = "0.0.0.0"
    port: int = 5000
    log_level: str = "INFO"

    class Config(BaseSettings.Config):
        env_prefix = "API_"


class MongoSettings(BaseSettings):
    uri: str = "mongodb://127.0.0.1:27017"
    database: str = "fastapi+pydantic+mongo-example"
    user_collection: str = "user"
    wallet_collection: str = "wallet"
    transaction_collection: str = "transaction"

    class Config(BaseSettings.Config):
        env_prefix = "MONGO_"

class JwtSettings(BaseSettings):
    secret: str = "secret"

    class Config(BaseSettings.Config):
        env_prefix = "JWT_"

api_settings = APISettings()
mongo_settings = MongoSettings()
jwt_settings = JwtSettings()
