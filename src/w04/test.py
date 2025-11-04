from src.w04.robot_audio import RobotAudio

if __name__ == '__main__':

    robot = RobotAudio()

    robot.send_audio_client("localhost")