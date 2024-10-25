# Visual Volume Control with Hand Tracking 🎯

This project demonstrates how to use **computer vision** to create a gesture-based volume controller. It uses **OpenCV** and **MediaPipe** to track hand gestures and adjust the system volume dynamically.

## Features ✨
- **Hand Tracking Module**: Detect and track hand landmarks using MediaPipe.
- **Coordinate Testing**: Retrieve and print landmark coordinates in real-time.
- **Finger Counter**: Detect the number of fingers shown using custom logic.
- **Volume Controller**: Adjust system volume based on the distance between two fingers.

## Technologies Used 🛠️
- Python 3.x  
- OpenCV  
- MediaPipe  
- Pycaw (for audio control)  

## Project Structure 📁
visual-volume-control/
│
├── HandTrackingModule.py       # Hand tracking logic encapsulated in a module
├── FingerCounter.py            # Detects number of fingers shown
├── VolumeControl.py            # Gesture-controlled volume adjustment
├── FingerImages/               # Folder containing images for finger counting
├── README.md                   # Project documentation (this file)file)


## How to Run the Project 🚀

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yaarya/visual-volume-control.git
   cd visual-volume-control

2. **Install Required Libraries:**
   ```bash
   pip install opencv-python-headless mediapipe comtypes numpy pycaw

3. **Run the Volume Controller:**
   ```bash
   python VolumeControl.py

## Usage 💡
- The program opens the webcam feed.
- Show two fingers (thumb + index) to adjust volume.
- Move fingers closer to reduce volume and spread them apart to increase it.
- Real-time FPS is displayed on the video feed.

## Possible Improvements 🔧
- Add gesture-based media controls (e.g., play/pause).
- Implement a GUI for smoother interaction.
- Integrate with smart home systems.
