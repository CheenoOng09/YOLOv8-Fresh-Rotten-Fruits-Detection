from ultralytics import YOLO
import cv2

cap = cv2.VideoCapture(0)  # 0 = default laptop camera
model = YOLO('yolov8_model3.pt')  # or your custom .pt file

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)
    annotated = results[0].plot()

    cv2.imshow('YOLOv8 Live', annotated)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
