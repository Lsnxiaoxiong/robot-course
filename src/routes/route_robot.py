import logging

from flask import Blueprint, Response, jsonify, request, current_app

from src.utils.resp import Result
from src.utils.robot_enum import ActionGroup
from src.w02.robot_manager import RobotManager

robot_bp = Blueprint('robot', __name__)
logger = logging.getLogger(__name__)


@robot_bp.route('/action/start', methods=['POST'])
def start_action() -> Response:
    robot_manager: RobotManager = current_app.robot_manager
    kwargs = request.get_json()
    action_name = kwargs.get('action_name', 'undefined')
    result: Result = robot_manager.start_action(action_name)
    return result


@robot_bp.route('/action/pause', methods=['POST'])
def pause_action() -> Response:
    robot_manager: RobotManager = current_app.robot_manager
    kwargs = request.get_json()
    action_name = kwargs.get('action_name', 'undefined')

    result: Result = robot_manager.pause_action(action_name)
    return result


@robot_bp.route('/action/resume', methods=['POST'])
def resume_action() -> Response:
    robot_manager: RobotManager = current_app.robot_manager
    kwargs = request.get_json()
    action_name = kwargs.get('action_name', 'undefined')

    result: Result = robot_manager.resume_action(action_name)
    return result


@robot_bp.route('/action/stop', methods=['POST'])
def stop_action() -> Response:
    robot_manager: RobotManager = current_app.robot_manager
    kwargs = request.get_json()
    action_name = kwargs.get('action_name', 'undefined')

    result: Result = robot_manager.stop_action(action_name)
    return result


@robot_bp.route('/robotTest', methods=['GET'])
def robot_test() -> Response:
    return Result.success("Robot is operational")