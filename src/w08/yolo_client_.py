
import cv2
import time
from ultralytics import YOLO

from src.utils.video_stream import get_frame
from src.w08.robot_rpc import RobotRPC

if __name__ == "__main__":
    # model = YOLO("yolo11n.pt")
    model = YOLO("../w06/YOLOv10n_gestures.pt")
    model.to("cuda")
    names = {0: 'grabbing', 1: 'grip', 2: 'holy', 3: 'point', 4: 'call', 5: 'three3', 6: 'timeout', 7: 'xsign', 8: 'hand_heart', 9: 'hand_heart2', 10: 'little_finger', 11: 'middle_finger', 12: 'take_picture', 13: 'dislike', 14: 'fist', 15: 'four', 16: 'like', 17: 'mute', 18: 'ok', 19: 'one', 20: 'palm', 21: 'peace', 22: 'peace_inverted', 23: 'rock', 24: 'stop', 25: 'stop_inverted', 26: 'three', 27: 'three2', 28: 'two_up', 29: 'two_up_inverted', 30: 'three_gun', 31: 'thumb_index', 32: 'thumb_index2', 33: 'no_gesture'}
    
    # 添加触发控制变量
    last_trigger_time = 0
    trigger_cooldown = 2  # 冷却时间2秒
    
    for frame in get_frame(ip="10.127.194.85", port=8888):
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
        results = model(frame, stream=True, conf=0.5)  # conf 设置置信度阈值
        for result in results:
            boxes = result.boxes.data.tolist()  # [[x_center, y_center, w, h, conf, cls],]
            
            # 检查是否有point手势（类别索引为3）
            point_detected = False
            # for box in boxes:
            #     if len(box) >= 6:  # 确保有足够的元素
            #         cls = int(box[5])  # 类别索引
            #         if cls == 3:  # 3对应"point"手势
            #             point_detected = True
            #             break
            #
            # # 如果检测到point手势且不在冷却期内
            # current_time = time.time()
            # if point_detected and (current_time - last_trigger_time > trigger_cooldown):
            #     try:
            #         response = RobotRPC.run_action("lie_down")
            #         print(f"检测到point手势，触发lie_down动作: {response}")
            #         last_trigger_time = current_time
            #     except Exception as e:
            #         print(f"调用机器人动作失败: {e}")
            
            annotated_frame = result.plot()
            cv2.imshow("YOLO11 Detection", annotated_frame)
