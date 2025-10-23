import threading
import time
import logging

from flask import Flask, jsonify, request
import hiwonder.ActionGroupControl as AGC
import hiwonder.ros_robot_controller_sdk as rrc
from hiwonder.Controller import Controller

from src.utils.resp import Result
from src.w02.robot_manager import RobotManager
from src.routes.route_robot import robot_bp


# 初始化Flask应用
# app = Flask(__name__)
# board = rrc.Board()
# ctl = Controller(board)

def init_logger() -> None:
    """
    初始化日志配置
    格式：yy-MM-dd hh:mm:ss name message
    """
    logging.basicConfig(
        level=logging.INFO,
        format="[%(levelname)s] %(asctime)s [%(name)s] ===> %(message)s",
        datefmt="%y-%m-%d %H:%M:%S"
    )

def create_app() -> Flask:
    app = Flask(__name__)
    init_logger()

    app.register_blueprint(robot_bp, url_prefix='/robot')
    app.robot_manager = RobotManager()

    return app


app = create_app()

if __name__ == '__main__':
    app = create_app()
    # 监听所有网络接口，这样局域网内的设备才能访问
    app.run(host='0.0.0.0', port=5000, debug=True)