from enum import Enum


class RobotRespCode(Enum):
    # 1000 - 1999 机器人动作错误
    ACTION_NOT_FOUND = 1000
    ACTION_ALREADY_RUNNING = 1001
    ACTION_IS_PAUSED = 1002
    ACTION_IS_STOPPED = 1003
    ACTION_IS_RUNNING = 1004


class ActionGroup(Enum):
    WALK_FORWARD = 'go_forward_one_step',
    DEMO = 'action_demo'


# 定义动作状态
class ActionStatus(Enum):
    CREATED = "CREATED"
    RUNNING = "RUNNING"
    PAUSED = "PAUSED"
    COMPLETED = "COMPLETED"
    STOPPED = "STOPPED"
    FAILED = "FAILED"