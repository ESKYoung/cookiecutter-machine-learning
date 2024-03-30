"""Define the settings for this project."""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Pydantic settings for this project."""

    DEBUG_MODE: bool = False
