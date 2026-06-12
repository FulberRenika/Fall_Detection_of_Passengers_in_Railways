from ultralytics import YOLO
import cv2

# Load trained model (best.pt)
model = YOLO(r"E:\datasets\best.pt")
# Test image
image_path = r"E:\datasets\train\images\images (8).jpg"       #train\images\2713919471_301fcc941f.jpg
results = model.predict(source=image_path, save=True, conf=0.25)
for r in results:
    img = r.plot()
    cv2.imshow("Prediction", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
