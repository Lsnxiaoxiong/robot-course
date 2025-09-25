import time
import threading
from enum import Enum


# 定义动作状态
class ActionEnum(Enum):
    INIT = "INIT"
    RUNNING = "RUNNING"
    PAUSED = "PAUSED"
    COMPLETED = "COMPLETED"
    STOPPED = "STOPPED"
    FAILED = "FAILED"


class Action:
    status: ActionEnum
    _thread: threading.Thread | None
    _run_event: threading.Event()
    _stop_event: threading.Event()
    name: str
    lock: threading.Lock()

    def __init__(self, name="undefined"):
        self.status = ActionEnum.INIT
        self._thread = None
        self._run_event = threading.Event()
        self._stop_event = threading.Event()
        self.name = name
        self.lock = threading.Lock()

    def is_init_status(self):
        return self.status == ActionEnum.INIT

    def is_undefined(self):
        return self.name == "undefined"

    def is_running(self):
        return self.status == ActionEnum.RUNNING

    def is_paused(self):
        return self.status == ActionEnum.PAUSED

    def is_stopped(self):
        return self._stop_event.is_set()

    def can_start(self):
        return (self.is_init_status() and
                (self._thread is None or not self._thread.is_alive()))

    def start(self):

        if not self.can_start():
            return
        with self.lock:
            if not self.can_start():
                return
            self.status = ActionEnum.RUNNING
            self._thread = threading.Thread(target=self.proxy_method, name=f"{self.name}-thread")
            self._run_event.set()
            self._thread.start()

    def pause(self):
        self.status = ActionEnum.PAUSED
        self._run_event.clear()

    def check_pause(self):
        self._run_event.wait()

    def resume(self):
        self.status = ActionEnum.RUNNING
        self._run_event.set()

    def before_stop(self):
        pass

    def stop(self):
        self.before_stop()
        self.status = ActionEnum.STOPPED
        self._stop_event.set()
        self._run_event.set()
        if self._thread:
            self._thread.join()
        self._thread = None

    def proxy_method(self) -> None:
        """
        eg:
        while not self.is_stopped():
            for i in range(100):
                self.check_pause()
                print(i)
                time.sleep(1)
        :return: None
        """
        raise NotImplementedError("Please implement the proxy_method in subclass")
