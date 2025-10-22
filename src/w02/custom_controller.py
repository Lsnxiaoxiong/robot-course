from src.w02.robot_action import Action
import hiwonder.ActionGroupControl as AGC


class CustomController(Action):
    action_name: str
    def __init__(self, action_name: str):
        super().__init__(action_name)
        self.action_name = action_name

    def run_action(self) -> None:
        while not self.is_stopped():
            AGC.runActionGroup(self.action_name)
            self.check_pause()

