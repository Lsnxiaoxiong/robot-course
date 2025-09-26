
from typing import Any, TypeVar

from flask import json, jsonify, Response, current_app


from src.utils.annotation import enforce_types
from src.w02.robot_manager import RobotRespCodeEnum


class Result:
    def __init__(self, code: int, message: str, data: Any) -> None:
        self.code = code
        self.message = message
        self.data = data

    @staticmethod
    def success(data: Any) -> Response: return Result(0, "success", data).to_json()

    @enforce_types
    @staticmethod
    def failed(robot_resp_code: RobotRespCodeEnum) -> Response:
        return Result(robot_resp_code.value, robot_resp_code.name, None).to_json()

    def to_json(self) -> Response:
        payload = {
            "code": self.code,
            "message": self.message,
            "data": self.data
        }

        return current_app.response_class(
            json.dumps(payload, default=default_serializer, ensure_ascii=False),
            mimetype='application/json'
        )


def default_serializer(obj: object) -> object:
    from enum import Enum
    from datetime import datetime
    import decimal, uuid

    if isinstance(obj, Enum):
        return obj.name
    if isinstance(obj, datetime):
        return obj.isoformat()
    if isinstance(obj, decimal.Decimal):
        return float(obj)
    if isinstance(obj, uuid.UUID):
        return str(obj)
    if hasattr(obj, "__dict__"):  # 普通自定义对象
        return obj.__dict__
    return str(obj)  # 兜底

