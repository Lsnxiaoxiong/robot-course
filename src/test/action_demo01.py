import time

from src.w02.robot_action import Action


class ActionDemo(Action):
    def __init__(self, name="action_demo"):
        super().__init__(name=name)

    def run_action(self):
        while not self.is_stopped():
            self.check_pause()
            print("hello")
            time.sleep(1)