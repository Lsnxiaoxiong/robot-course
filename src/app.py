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

    # === 全局返回拦截器 ===
    # @app.after_request
    # def wrap_response(response):
    #     """
    #     如果返回值是 Result，就自动转 jsonify
    #     """
    #     print("==============>")
    #     # Flask 的 Response 对象就不动
    #     if response is None or hasattr(response, "status_code"):
    #         return response

    #     # 如果是 Result 类型 -> 转成 jsonify
    #     if isinstance(response, Result):
    #         return response.to_json()

    #     return response

    app.register_blueprint(robot_bp, url_prefix='/robot')
    app.robot_manager = RobotManager()

    return app


app = create_app()

# 创建一个API端点来执行动作
# 可以通过访问 http://<树莓派IP>:5000/run_action/stand 来让机器人站立
# @app.route('/run_action/<string:action_name>', methods=['GET'])
# def run_robot_action(action_name):
#     try:
#         print(f"接收到指令，执行动作: {action_name}")
#         # 直接调用您SDK中的函数
#         # 注意：这里的路径需要是机器人的实际路径，如果SDK默认值正确则无需修改
#         AGC.runActionGroup(action_name, times=5, with_stand=True)

#         return jsonify({"status": "success", "action": action_name})
#     except Exception as e:
#         print(f"执行动作失败: {e}")
#         return jsonify({"status": "error", "message": str(e)}), 500





if __name__ == '__main__':
    app = create_app()
    # 监听所有网络接口，这样局域网内的设备才能访问
    app.run(host='0.0.0.0', port=5000, debug=True)