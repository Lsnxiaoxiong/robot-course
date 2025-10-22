import logging
import threading

from flask import Blueprint, Response, jsonify, request, current_app

from src.utils.resp import Result
from src.utils.robot_enum import ActionGroup
from src.w02.robot_manager import RobotManager
from hiwonder.Controller import Controller
import hiwonder.ros_robot_controller_sdk as rrc


robot_bp = Blueprint('robot', __name__)
logger = logging.getLogger(__name__)

board = rrc.Board()
ctl = Controller(board)

@robot_bp.route('/action/start', methods=['POST'])
def start_action() -> Response:
    robot_manager: RobotManager = current_app.robot_manager
    kwargs = request.get_json()
    action_name = kwargs.get('action_name', 'undefined')
    resp: Response = robot_manager.start_action(action_name)
    return resp


@robot_bp.route('/action/pause', methods=['POST'])
def pause_action() -> Response:
    robot_manager: RobotManager = current_app.robot_manager
    kwargs = request.get_json()
    action_name = kwargs.get('action_name', 'undefined')

    resp: Response = robot_manager.pause_action(action_name)
    return resp


@robot_bp.route('/action/resume', methods=['POST'])
def resume_action() -> Response:
    robot_manager: RobotManager = current_app.robot_manager
    kwargs = request.get_json()
    action_name = kwargs.get('action_name', 'undefined')

    resp: Response = robot_manager.resume_action(action_name)
    return resp


@robot_bp.route('/action/stop', methods=['POST'])
def stop_action() -> Response:
    robot_manager: RobotManager = current_app.robot_manager
    kwargs = request.get_json()
    action_name = kwargs.get('action_name', 'undefined')

    resp: Response = robot_manager.stop_action(action_name)
    return resp

@robot_bp.route('/turn_head', methods=['POST'])
def turn_head() -> Response:
    """
    控制舵机转动到指定位置
         servo_id: 要驱动的舵机id(the servo id needed to be driven)
         pulse: 舵机目标位置(servo target position)
            上下转动的舵机限制角度在130°左右，左右180°，范围在500-2500之间。
         use_time: 转动需要的时间(the time needed to rotate)
    eg:
        ctl.set_pwm_servo_pulse(servo_id=1, pulse=1700, use_time=500) # 上下转头
        ctl.set_pwm_servo_pulse(servo_id=2, pulse=1400, use_time=500) # 左右转头
    :return: 返回JSON响应，包含操作状态和参数
    """
    req_data = request.get_json()
    servo_id = req_data.get('servo_id')
    pulse = req_data.get('pulse')
    threading.Thread(target=ctl.set_pwm_servo_pulse, args=(servo_id, pulse, 500)).start()
    return Result.success(data={
        "servo_id": servo_id,
        "pulse": pulse
    })


@robot_bp.route('/robotTest', methods=['GET'])
def robot_test() -> Response:
    return Result.success("Robot is operational")