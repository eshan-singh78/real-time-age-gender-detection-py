# Live Gender and Age Detection using OpenCV and DeepFace

This Python script captures video from the default camera and detects the gender and age of people in real-time using OpenCV and DeepFace.

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/eshan-singh78/real-time-age-gender-detection-py.git
   ```

2. Navigate to the project directory:
   ```
   cd your_repository
   ```

3. Install the required dependencies:
   ```
   pip install opencv-python
   pip install deepface
   ```

## Usage

Run the Python script `deepcvfaceage.py`:
   ```
   python deepcvfaceage.py
   ```

Press 'q' to exit the program.

## Description

This script uses the `cv2` library to capture video from the default camera. It then uses the `DeepFace` library to detect faces in the frames and analyze them for gender and age. The script continuously displays the video feed and prints the gender and age of detected faces.

## Credits

- [OpenCV](https://opencv.org/)
- [DeepFace](https://github.com/serengil/deepface)
