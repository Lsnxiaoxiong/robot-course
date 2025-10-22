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
def turn_head():
    req_data = request.get_json()
    servo_id = req_data.get('servo_id')
    pulse = req_data.get('pulse')
    # ctl.set_pwm_servo_pulse(servo_id, pulse, 500)
    threading.Thread(target=ctl.set_pwm_servo_pulse, args=(servo_id, pulse, 500)).start()
    # return jsonify({"status": "success", "servo_id": servo_id, "pulse": pulse})
    return Result.success(data={
        "servo_id": servo_id,
        "pulse": pulse
    })


@robot_bp.route('/robotTest', methods=['GET'])
def robot_test() -> Response:
    return Result.success("Robot is operational")