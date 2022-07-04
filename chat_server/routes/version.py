import io
import os
from typing import Literal

from fastapi import APIRouter

from chat_server.exceptions.base_errors import ValidateError
from chat_server.serializers.version import VersionReturnSerializer
from chat_server.utils.route import CustomRoute

router = APIRouter(route_class=CustomRoute)


@router.get('/version')
def version() -> VersionReturnSerializer:
    """
    # 读取版本号
    """
    with io.open(
            os.path.join(os.path.dirname(__file__), '..', "VERSION"),
            encoding="utf8",
    ) as open_file:
        content = open_file.read().strip()
    return VersionReturnSerializer(version=content)
