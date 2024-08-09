# Drowsiness Detection System

## Overview

The Drowsiness Detection System is a real-time application that monitors driver alertness by analyzing eye aspect ratio (EAR) using facial landmarks. The system detects if the user's eyes are closed for an extended period and triggers an alert to ensure safety.

## Features

- **Real-time Eye Aspect Ratio Calculation:** Computes EAR using facial landmarks.
- **Alert System:** Displays an alert message and plays a sound if drowsiness is detected.
- **Face Detection:** Identifies faces in the video feed using `dlib`.
- **Eye Contour Visualization:** Draws contours around detected eyes.

## Requirements

- Python 3.x
- OpenCV
- imutils
- dlib
- pygame
- scipy

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/username/repository.git
   cd repository
   ```
2. **Install Required Libraries:**

   ```bash
   pip install -r requirements.txt
   ```
3. **Download Pre-trained Models:**
  Download the shape_predictor_68_face_landmarks.dat file from dlib's model repository and place it in the models/ directory.
4. **Prepare Audio File:**
Ensure you have a music.wav file in the project directory for the alert sound.

## Usage

1. **Run the Script:**
   ```bash
   Drowsiness_Detection.py
   ```
2. **Interaction:**
- The script opens your webcam and starts processing the video feed.
- If the eye aspect ratio (EAR) falls below the threshold for a set number of frames, an alert message will be displayed on the screen, and an audio alert will sound.
- Press q to quit the application.

## Code Explanation
- **eye_aspect_ratio(eye):** Calculates the EAR for a given eye region.
- **thresh:** EAR threshold below which an alert is triggered.
- **frame_check:** Number of frames with EAR below the threshold before triggering an alert.
- **detect:** Face detector initialized from dlib.
- **predict:** Shape predictor for facial landmarks.
## Report
[Report](https://github.com/user-attachments/files/16555561/CG_report.1.1.pdf)

## Contributing
Contributions are welcome! Please open issues or submit pull requests to improve the project.
