from src.w02.robot_action import Action
import hiwonder.ActionGroupControl as AGC


class WalkController(Action):
    name: str

    def __init__(self, name: str = "walk_controller") -> None:
        super().__init__(name=name)
        self.name = name

    def run_action(self) -> None:
        while not self.is_stopped():
            self.check_pause()
            AGC.runActionGroup('go_forward_one_step')
