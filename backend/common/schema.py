from datetime import datetime
from typing import Annotated

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field

from backend.utils.timezone import timezone

CustomPhoneNumber = Annotated[str, Field(pattern=r'^1[3-9]\d{9}$')]


class SchemaBase(BaseModel):
    """基础模型配置"""

    model_config = ConfigDict(
        use_enum_values=True,
        json_encoders={
            datetime: lambda x: timezone.to_str(timezone.from_datetime(x))
            if x.tzinfo is not None
            else timezone.to_str(x)
        },
    )
