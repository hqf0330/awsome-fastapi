from fastapi import FastAPI
from backend.utils.serializers import MsgSepcJSONResponse
from backend.core.conf import settings


def register_app() -> FastAPI:
    app = FastAPI(
        title=settings.FASTAPI_TITLE,
        version=settings.FASTAPI_VERSION,
        description=settings.FASTAPI_DESCRIPTION,
        docs_url=settings.FASTAPI_DOCS_URL,
        redoc_url=settings.FASTAPI_REDOC_URL,
        openapi_url=settings.FASTAPI_OPENAPI_URL,
        default_response_class=MsgSepcJSONResponse,
        # lifespan=
    )
    return app