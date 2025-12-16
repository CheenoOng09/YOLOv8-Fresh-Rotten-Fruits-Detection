# Fresh and Rotten Vegetable Detection using YOLOv8

**Authors:** 
- Mikollito Ong
- 徐葆翰
- 
**Institution:** Yuan Ze University (元智大学)  
**Project Type:** Final Year / Capstone Project  

---

## Overview

This project focuses on detecting and classifying **fresh and rotten vegetables** using a deep learning–based object detection model built on **YOLOv8**. The goal is to automate quality inspection in grocery and supply-chain environments by accurately identifying vegetable types and their freshness state in real time.

The system was developed as a final-year university project and demonstrates an end-to-end machine learning workflow, including dataset preparation, training, evaluation, and live inference using a camera feed.

---

## Key Features

- Real-time object detection using **YOLOv8**
- Classification of vegetables into **fresh** and **rotten/expired** categories
- High detection accuracy across most classes
- Supports live webcam inference
- Designed for future automation and smart inspection systems

---

## Dataset

### Final Class List

The model was trained on the following **14 classes**:

- bellpepper_fresh  
- bellpepper_rotten  
- bitter_gourd_fresh  
- bitter_gourd_rotten  
- capsicum_fresh  
- capsicum_rotten  
- carrot_fresh  
- carrot_rotten  
- cucumber_fresh  
- cucumber_rotten  
- okra_fresh  
- okra_rotten  
- potato_fresh  
- potato_expired  

### Dataset Sources

- **Primary Dataset:**  
  Fruits and Vegetables Dataset (Kaggle)  
  https://www.kaggle.com/datasets/muhriddinmuxiddinov/fruits-and-vegetables-dataset  

- **Secondary Dataset:**  
  Additional classes (Capsicum, Bitter Gourd, Okra) were sourced from a separate Kaggle dataset.  
  The original link is no longer available, and the dataset is **not redistributed** in this repository.

### Exclusions and Notes

- **Tomatoes (fresh and rotten)** were intentionally excluded from the final dataset.
- Capsicum was treated as a separate class from bell pepper, which introduced some label ambiguity.
- Images were **manually annotated** to ensure correct freshness labeling.

### Dataset Split

- 80% Training  
- 10% Validation  
- 10% Testing  

---

## Training Configuration

- **Model:** YOLOv8m (pre-trained on COCO)
- **Framework:** Ultralytics YOLOv8 (PyTorch)
- **Epochs:** 150
- **Batch Size:** 16
- **Image Size:** 640 × 640
- **Optimizer:** SGD (auto)
- **Learning Rate:** 0.01
- **Momentum:** 0.937
- **Weight Decay:** 0.0005

### Loss Weights
- Bounding Box Loss: 7.5  
- Classification Loss: 0.5  
- Distribution Focal Loss (DFL): 1.5  

---

## Data Preprocessing & Augmentation

- Image resizing to 640 × 640
- Mosaic augmentation enabled
- Horizontal flip (50% probability)
- HSV adjustments:
  - Saturation: 0.7
  - Brightness: 0.4
- Dataset integrity checks and class relabeling handled via helper scripts

## Evaluation Metrics & Results

### Quantitative Performance

- **mAP@50:** **0.905**
- **Overall F1-score:** ~**0.86**

### Observations

- Bitter gourd (fresh and rotten) achieved near-perfect classification performance.
- Bell pepper and cucumber classes showed strong precision and recall.
- Potato_expired and some capsicum classes exhibited lower precision.
- Some vegetables were misclassified as background, indicating room for improvement in background separation.

### Training Behavior

- Training and validation losses decreased consistently over 150 epochs.
- Validation trends closely followed training loss, suggesting **minimal overfitting**.
- The model converged stably and achieved optimal performance near the end of training.

---

## Inference

### Run Image Inference
```bash
python infer.py --weights weights/best.pt --source path/to/image_or_folder
```

### Live Webcam Demo

```bash
python scripts/app.py --weights weights/best.pt
```

---

## Repository Structure

- scripts/ – training, inference, and helper scripts
- weights/ – trained model (`best.pt`)
- assets/ – evaluation plots and metrics
- docs/ – project report and poster
- requirements.txt – dependencies

---

## License

This project is released under the **MIT License**.

