from fastapi import APIRouter

def build_final_router() -> APIRouter:
    """
    最终路由
    TODO: 扩展插件路由
    """
    from backend.app.router import router as main_router
    return main_router