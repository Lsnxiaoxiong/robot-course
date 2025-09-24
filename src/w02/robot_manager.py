from enum import Enum

from src.w02.robot_action import Action


class ActionGroupEnum(Enum):
    WALK_FORWARD = 'go_forward_one_step'

class RobotManager:
    def __init__(self):
        self.action_dict: dict[str, Action] = {}

    def init_action_dict(self) -> None:
        for action in ActionGroupEnum:
            self.action_dict[action.value] = Action()

    def start_action(self, action:ActionGroupEnum = None):
        if not isinstance(action,ActionGroupEnum):
            raise Exception("The input parameter 'action' should be an instance of ActionEnum")

        if not self.action_dict[action.value].is_undefined():
            return




if __name__ == '__main__':
    rm = RobotManager()
    # rm.start_action('go_forward_one_step')
    print(rm.action_dict)
