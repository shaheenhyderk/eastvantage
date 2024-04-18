from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "East Vantage Test"
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///./data.db"
    ROOT_URL_PREFIX: str = '/api/v1'


settings = Settings()
