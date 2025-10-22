import time
import threading
from enum import Enum
from typing import Optional



# 定义动作状态
class ActionEnum(Enum):
    CREATED = "CREATED"
    RUNNING = "RUNNING"
    PAUSED = "PAUSED"
    COMPLETED = "COMPLETED"
    STOPPED = "STOPPED"
    FAILED = "FAILED"


class Action:
    _status: ActionEnum
    _thread: Optional[threading.Thread]
    _run_event: threading.Event
    _stop_event: threading.Event
    _lock: threading.Lock
    name: str

    def __init__(self, name="undefined") -> None:
        self._status = ActionEnum.CREATED
        self._thread = None
        self._run_event = threading.Event()
        self._stop_event = threading.Event()
        self._lock = threading.Lock()
        self.name = name

    def is_created(self) -> bool:
        return self._status == ActionEnum.CREATED

    def is_undefined(self) -> bool:
        return self.name == "undefined"

    def is_running(self) -> bool:
        return self._status == ActionEnum.RUNNING

    def is_paused(self) -> bool:
        return self._status == ActionEnum.PAUSED

    def is_stopped(self) -> bool:
        return self._stop_event.is_set()

    def can_start(self) -> bool:
        if self.is_running():
            return False
        if self.is_paused():
            return False
        if self._thread is not None and self._thread.is_alive():
            return False
        return True

    def start(self) -> None:
        if not self.can_start():
            return
        with self._lock:
            if not self.can_start():
                return
            self._stop_event.clear()
            self._status = ActionEnum.RUNNING
            self._run_event.set()
            try:
                self._thread = threading.Thread(target=self.run_action, name=f"{self.name}-thread")
                self._thread.start()
            except:
                self._status = ActionEnum.FAILED
                self._thread = None
                self._run_event.clear()
                raise RuntimeError("Failed to start the thread")

    def pause(self) -> None:
        self._status = ActionEnum.PAUSED
        self._run_event.clear()

    def check_pause(self) -> None:
        self._run_event.wait()

    def resume(self) -> None:
        self._status = ActionEnum.RUNNING
        self._run_event.set()

    def before_stop(self) -> None:
        pass

    def stop(self) -> None:
        self.before_stop()
        self._status = ActionEnum.STOPPED
        self._stop_event.set()
        self._run_event.set()
        if self._thread:
            self._thread.join()
        self._thread = None

    def run_action(self) -> None:
        """
        eg:
        while not self.is_stopped():
            for i in range(100):
                self.check_pause()
                print(i)
                time.sleep(1)
        :return: None
        """
        raise NotImplementedError("Please implement the run_action in subclass")
