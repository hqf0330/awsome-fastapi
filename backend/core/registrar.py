from fastapi import Depends, FastAPI
from backend.utils.serializers import MsgSpecJSONResponse
from backend.core.conf import settings
from backend.plugin.tools import build_final_router
from backend.utils.demo_site import demo_site
from backend.utils.health_check import ensure_unique_route_names


def register_app() -> FastAPI:
    app = FastAPI(
        title=settings.FASTAPI_TITLE,
        version=settings.FASTAPI_VERSION,
        description=settings.FASTAPI_DESCRIPTION,
        docs_url=settings.FASTAPI_DOCS_URL,
        redoc_url=settings.FASTAPI_REDOC_URL,
        openapi_url=settings.FASTAPI_OPENAPI_URL,
        default_response_class=MsgSpecJSONResponse,
        # lifespan=
    )

    # 注册路由
    register_router(app)

    return app


def register_router(app: FastAPI) -> None:
    """
    注册路由
    :param app: FASTAPI
    :return:
    """
    dependencies = [Depends(demo_site)] if settings.DEMO_MODE else None

    # 注册路由
    router = build_final_router()
    app.include_router(router, dependencies=dependencies)

    # 额外
    ensure_unique_route_names(app)


