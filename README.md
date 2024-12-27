# 🎾 Tennis Analysis Project

## 📜 Introduction

This project focuses on analyzing tennis players' performance from videos by measuring:

- Player speed
- Ball shot speed
- Number of shots

The system detects players and tennis balls using YOLO and extracts court keypoints using CNNs. This hands-on project is ideal for enhancing your skills in **Machine Learning** and **Computer Vision**.

---

## 📽 Output Videos

Here is a screenshot from one of the output videos:

<img width="1005" alt="image" src="https://github.com/user-attachments/assets/ac896515-8640-4d74-9026-2b3536d8c4c8" />

---

## 🧠 Models Used

1. **Player Detection**: YOLO v8
2. **Tennis Ball Detection**: Fine-tuned YOLO
3. **Court Keypoint Extraction**: ResNet50

### Trained Models:

- [YOLOv5 Tennis Ball Detector](https://drive.google.com/file/d/1UZwiG1jkWgce9lNhxJ2L0NVjX1vGM05U/view?usp=sharing)
- [Tennis Court Keypoint Detector](https://drive.google.com/file/d/1QrTOF1ToQ4plsSZbkBs3zOLkVt3MBlta/view?usp=sharing)

---

## 🏋️‍♂️ Training

- **Tennis Ball Detector**: [`training/tennis_ball_detector_training.ipynb`](training/tennis_ball_detector_training.ipynb)
- **Tennis Court Keypoint Model**: [`training/tennis_court_keypoints_training.ipynb`](training/tennis_court_keypoints_training.ipynb)

---

## 📋 Requirements

Make sure you have the following installed:

- Python 3.8+
- [Ultralytics](https://github.com/ultralytics/yolov5)
- PyTorch
- Pandas
- NumPy
- OpenCV
