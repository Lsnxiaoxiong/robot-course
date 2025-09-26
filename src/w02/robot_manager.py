import time
from enum import Enum
from typing import Optional
import threading

from src.test.action_demo01 import ActionDemo
from src.utils.annotation import enforce_types
from src.w02.robot_action import Action, ActionEnum


# from src.w02.walk_controller import WalkController


class ActionGroupEnum(Enum):
    WALK_FORWARD = 'go_forward_one_step',
    DEMO = 'action_demo'


class RobotManager:
    def __init__(self) -> None:
        self.action_dict: dict[ActionGroupEnum, Action] = {
            # ActionGroupEnum.WALK_FORWARD: WalkController(),
            ActionGroupEnum.DEMO: ActionDemo(),
        }

    @enforce_types
    def start_action(self, action: Optional[ActionGroupEnum]) -> None:
        self.action_dict[action].start()

    @enforce_types
    def stop_action(self, action: Optional[ActionGroupEnum]) -> None:
        if self.action_dict[action].is_undefined():
            return
        self.action_dict[action].stop()

    @enforce_types
    def pause_action(self, action: Optional[ActionGroupEnum]) -> None:
        if self.action_dict[action].is_undefined():
            return
        self.action_dict[action].pause()

    @enforce_types
    def resume_action(self, action: Optional[ActionGroupEnum]) -> None:
        if self.action_dict[action].is_undefined():
            return
        self.action_dict[action].resume()


if __name__ == '__main__':
    rm = RobotManager()
    rm.start_action(ActionGroupEnum.DEMO)
    # print(rm.action_dict)
    time.sleep(5)

    rm.pause_action(ActionGroupEnum.DEMO)
    time.sleep(5)
    rm.resume_action(ActionGroupEnum.DEMO)
    time.sleep(5)
    rm.stop_action(ActionGroupEnum.DEMO)
