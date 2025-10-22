from enum import Enum

from src.w02.custom_controller import CustomController


class RobotRespCode(Enum):
    # 1000 - 1999 机器人动作错误
    ACTION_NOT_FOUND = 1000
    ACTION_ALREADY_RUNNING = 1001
    ACTION_IS_PAUSED = 1002
    ACTION_IS_STOPPED = 1003
    ACTION_IS_RUNNING = 1004

    # 2000 - 2999 运行错误
    MISSING_PARAMETER = 2000


class ActionGroup(Enum):
    """
    机器人动作组，name对应Tonypi/ActionGroups库中的动作组名称，仅配置可循环执行的动作
    """
    WALK_FORWARD = 'go_forward_one_step'
    RIGHT_MOVE = 'right_move_40'
    LEFT_MOVE = 'left_move_40'
    BACK_ONE_STEP = 'back_one_step'
    TURN_LEFT = 'turn_left'
    TURN_RIGHT = 'turn_right'

    def __init__(self, action_name: str):
        self.action_name = action_name




# 定义动作状态
class ActionStatus(Enum):
    CREATED = "CREATED"
    RUNNING = "RUNNING"
    PAUSED = "PAUSED"
    COMPLETED = "COMPLETED"
    STOPPED = "STOPPED"
    FAILED = "FAILED"


