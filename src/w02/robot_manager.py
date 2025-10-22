import logging
import time
from enum import Enum
from typing import Optional
import threading

from flask import Response

from src.test.action_demo01 import ActionDemo
from src.utils.annotation import enforce_types
from src.utils.resp import Result
from src.utils.robot_enum import ActionGroup, RobotRespCode
from src.w02.custom_controller import CustomController
from src.w02.robot_action import Action, ActionEnum
from src.w02.s05_flow_control import actions
from src.w02.walk_controller import WalkController

# from src.w02.walk_controller import WalkController


logger = logging.getLogger(__name__)


class RobotManager:
    """
    机器人动作管理器
    """
    def __init__(self) -> None:
        self.action_dict: dict[ActionGroup, Action] = {
            # ActionGroup.WALK_FORWARD: WalkController(),
            # ActionGroup.DEMO: ActionDemo(),
        action: CustomController(action.action_name)
        for action in ActionGroup
        }

    @enforce_types
    def start_action(self, action_name: str) -> Response:
        """
        启动机器人动作
        :param action_name: 动作名称。从ActionGroup枚举类中选择。
        :return: Response对象，包含操作结果。
        """
        if action_name not in ActionGroup.__members__:
            return Result.failed(RobotRespCode.ACTION_NOT_FOUND)
        action: Action = self.action_dict[ActionGroup[action_name]]

        if action.is_running() or not action.can_start():
            return Result.failed(RobotRespCode.ACTION_ALREADY_RUNNING)

        logger.info(f"Starting action: {ActionGroup[action_name]}")
        self.action_dict[ActionGroup[action_name]].start()
        return Result.success(ActionGroup[action_name])

    @enforce_types
    def stop_action(self, action_name: str) -> Response:
        if action_name not in ActionGroup.__members__:
            return Result.failed(RobotRespCode.ACTION_NOT_FOUND)
        logger.info(f"Stop action: {ActionGroup[action_name]}")
        self.action_dict[ActionGroup[action_name]].stop()
        return Result.success(ActionGroup[action_name])

    @enforce_types
    def pause_action(self, action_name: str) -> Response:
        if action_name not in ActionGroup.__members__:
            return Result.failed(RobotRespCode.ACTION_NOT_FOUND)
        logger.info(f"Pause action: {ActionGroup[action_name]}")
        self.action_dict[ActionGroup[action_name]].pause()
        return Result.success(ActionGroup[action_name])

    @enforce_types
    def resume_action(self, action_name: str) -> Response:
        if action_name not in ActionGroup.__members__:
            return Result.failed(RobotRespCode.ACTION_NOT_FOUND)
        logger.info(f"Resume action: {ActionGroup[action_name]}")
        self.action_dict[ActionGroup[action_name]].resume()
        return Result.success(ActionGroup[action_name])



