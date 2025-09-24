from src.w02.robot_action import Action
import hiwonder.ActionGroupControl as AGC

class WalkController(Action):
    def __init__(self, name="walk_controller"):
        super().__init__(name=name)

    def proxy_method(self):
        while not self.is_stopped():
            self.check_pause()
            AGC.runActionGroup('go_forward_one_step')



