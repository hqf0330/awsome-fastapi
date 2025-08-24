from functools import lru_cache
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict
from backend.core.path_conf import BASE_PATH


class Settings(BaseSettings):
    """
    全局配置
    """
    model_config = SettingsConfigDict(
        env_file=f'{BASE_PATH}/.env',
        env_file_encoding='utf-8',
        extra='ignore',
        case_sensitive=True
    )

    # .env当前环境
    ENVIRONMENT: Literal['dev', 'prod']

    # FastAPI
    FASTAPI_API_V1_PATH: str = '/api/v1'
    FASTAPI_TITLE: str = 'FastAPI'
    FASTAPI_VERSION: str = '1.5.0'
    FASTAPI_DESCRIPTION: str = 'FastAPI Best Architecture'
    FASTAPI_DOCS_URL: str = '/docs'
    FASTAPI_REDOC_URL: str = '/redoc'
    FASTAPI_OPENAPI_URL: str | None = '/openapi'
    FASTAPI_STATIC_FILES: bool = True

    # 时间配置
    DATETIME_TIMEZONE: str = 'Asia/Shanghai'
    DATETIME_FORMAT: str = '%Y-%m-%d %H:%M:%S'


@lru_cache
def get_settings() -> Settings:
    """
    获取全局配置单例
    """
    return Settings() # type: ignore

# 创建全局
settings = get_settings()