from ultralytics import YOLO

model = YOLO('yolov8x')
# model = YOLO('./models/last.pt')

result = model.track('./input-videos/input_video.mp4', save=True)

print(result)
print("----------------------")
for box in result[0].boxes:
    print(box)