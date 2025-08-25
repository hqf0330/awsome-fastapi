
from fastapi import APIRouter

from backend.common.response.response_schema import ResponseModel
from backend.common.response.response_schema import response_base

router = APIRouter()

@router.get('/me', summary='获取当前用户信息',)
async def get_current_user() -> ResponseModel:
    return response_base.success(data="success")