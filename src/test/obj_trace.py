import cv2

# 打开视频（或使用摄像头）
cap = cv2.VideoCapture("stree.mp4")  # 可改成 "video.mp4"

# 读取第一帧
ret, frame = cap.read()
if not ret:
    print("无法读取视频源")
    exit()

# 手动选择跟踪目标（ROI：Region of Interest）
bbox = cv2.selectROI("请选择跟踪目标", frame, fromCenter=False, showCrosshair=True)
cv2.destroyWindow("请选择跟踪目标")

# 创建跟踪器（推荐 CSRT）
tracker = cv2.legacy.TrackerCSRT_create()
ok = tracker.init(frame, bbox)

# 逐帧更新跟踪
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 更新跟踪结果
    ok, bbox = tracker.update(frame)

    if ok:
        # 如果成功跟踪，绘制矩形框
        x, y, w, h = map(int, bbox)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, "Tracking", (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    else:
        # 跟踪失败
        cv2.putText(frame, "Lost", (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    cv2.imshow("Object Tracking", frame)

    # 按 ESC 退出
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
