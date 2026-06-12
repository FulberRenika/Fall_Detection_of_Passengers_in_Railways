# from ultralytics import YOLO
# import cv2
# import time

# # ====== CONFIG ======
# MODEL_PATH = r"E:\datasets\best.pt"   # change if your path is different
# CAM_INDEX = 0                              # 0 = default webcam
# CONF = 0.25                                # confidence threshold
# IMG_SIZE = 640                             # inference image size
# # ====================

# def main():
#     # Load model
#     model = YOLO(MODEL_PATH)

#     # Open webcam
#     cap = cv2.VideoCapture(CAM_INDEX)
#     if not cap.isOpened():
#         print(f"❌ Could not open webcam (index={CAM_INDEX}). Try CAM_INDEX=1 or 2.")
#         return

#     # Optional: set camera resolution (comment out if it causes issues)
#     cap.set(cv2.CAP_PROP_FRAME_WIDTH,  1280)
#     cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

#     prev_time = time.time()

#     print("✅ Realtime detection started.")
#     print("Press 'q' to quit.")

#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             print("❌ Failed to read frame from webcam.")
#             break

#         # YOLO prediction on the frame
#         results = model.predict(source=frame, imgsz=IMG_SIZE, conf=CONF, verbose=False)

#         # Draw boxes on frame
#         annotated = results[0].plot()

#         # FPS display
#         curr_time = time.time()
#         fps = 1.0 / (curr_time - prev_time) if curr_time != prev_time else 0.0
#         prev_time = curr_time

#         cv2.putText(
#             annotated,
#             f"FPS: {fps:.1f}",
#             (15, 35),
#             cv2.FONT_HERSHEY_SIMPLEX,
#             1,
#             (0, 255, 0),
#             2
#         )

#         cv2.imshow("YOLO Realtime (press q to quit)", annotated)

#         # Quit
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     cap.release()
#     cv2.destroyAllWindows()
#     print("👋 Closed.")

# if __name__ == "__main__":
#     main()







# part 2


from ultralytics import YOLO
import cv2
import time

# Windows beep
import winsound

model = YOLO("best.pt")   # change path if needed
cap = cv2.VideoCapture(0)

CONF = 0.5
BEEP_GAP = 1.0     # seconds between beeps (prevents continuous noise)
last_beep = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, conf=CONF, verbose=False)

    danger = False

    for r in results:
        if r.boxes is None:
            continue
        for box in r.boxes:
            cls = int(box.cls[0])
            conf = float(box.conf[0])

            # IMPORTANT: Assuming class 1 = danger
            if cls == 1 and conf >= CONF:
                danger = True

    now = time.time()

    if danger:
        cv2.putText(frame, "Danger", (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
        if now - last_beep > BEEP_GAP:
            winsound.Beep(1200, 200)  # frequency, duration(ms)
            last_beep = now
    else:
        cv2.putText(frame, "Normal", (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    cv2.imshow("Edge Safety Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()