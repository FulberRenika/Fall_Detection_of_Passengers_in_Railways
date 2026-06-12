## Overview

This project aims to improve railway passenger safety by detecting fall incidents in real-time using YOLOv8 and Computer Vision techniques.
The system analyzes video frames and identifies passengers who may have fallen onto railway tracks or platforms. Early detection can help railway authorities respond quickly and prevent accidents.

## Problem Statement

Passenger falls in railway stations and near railway tracks can lead to serious injuries and fatalities.
Manual monitoring of CCTV footage is difficult and may delay emergency response.
This project proposes an automated fall detection system using YOLOv8 to identify potential fall incidents in real time.

## Objectives

* Detect passengers in railway environments.
* Identify fall incidents using Computer Vision.
* Provide real-time monitoring support.
* Improve passenger safety through early alerts.

## Technologies Used

* Python
* YOLOv8 (Ultralytics)
* OpenCV
* Google Colab
* Computer Vision

## Dataset

The dataset consists of railway passenger images and video frames containing normal and fall scenarios.
Dataset was preprocessed and converted into YOLO format for training.

## Model Training

* Model: YOLOv8
* Framework: Ultralytics
* Image Size: 640 × 640
* Training Environment: Google Colab GPU

## Results

The trained model successfully detects passengers and identifies fall situations in test images and videos.

### Sample Outputs

![Results](https://github.com/FulberRenika/Fall_Detection_of_Passengers_in_Railways/blob/main/Example1.png?raw=true)

## Future Improvements

* Real-time CCTV integration
* Alert notification system
* Railway control room dashboard
* Mobile application support

## Contributors

* Fulber Renika C R
* Aarthi V
* Ganga S
* Akshaya K

## License

This project is developed for academic and educational purposes.
