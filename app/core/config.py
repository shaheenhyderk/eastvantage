from pathlib import Path

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "East Vantage Test"
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///./data.db"
    ROOT_URL_PREFIX: str = '/api/v1'

    BASE_DIR: Path = Path(__file__).resolve().parent.parent.parent
    # Log path can be moved to env so that we can use diff path in diff env such as /var/log/..
    LOG_DIR: Path = BASE_DIR / 'logs'


# A temp function to create logs dir
def ensure_log_dir_exists(log_dir: Path):
    if not log_dir.exists():
        log_dir.mkdir(parents=True, exist_ok=True)


settings = Settings()
ensure_log_dir_exists(settings.LOG_DIR)
