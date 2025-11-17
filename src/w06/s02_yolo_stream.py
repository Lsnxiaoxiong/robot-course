from ultralytics import YOLO
import cv2

model = YOLO("yolo11n.pt")
cap = cv2.VideoCapture(0)

# 设置视频流参数（可选）
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while cap.isOpened():
    success, frame = cap.read()

    if success:
        # 使用 stream=True 可以提高处理速度
        results = model(frame, stream=True, conf=0.5)  # conf 设置置信度阈值

        for result in results:
            annotated_frame = result.plot()
            cv2.imshow("YOLO11 Detection", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
