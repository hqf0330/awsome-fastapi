from typing import Any
from msgspec import json
from starlette.responses import JSONResponse


class MsgSepcJSONResponse(JSONResponse):
    """
    将数据序列化为JSON的响应类
    """
    def render(self, content: Any) -> bytes:
        return json.encode(content)