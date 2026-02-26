The Eye-Mouse project is an advanced Human-Computer Interaction (HCI) system designed to bridge the gap between physical movement and digital navigation. By leveraging the power of Artificial Intelligence and Real-time Computer Vision, this application allows users to control their computer's mouse cursor using only their eyes and facial gestures.

In a world where accessibility is becoming a priority, this project serves as a foundational tool for individuals with motor impairments or those looking for a futuristic, hands-free way to interact with their operating systems. The system captures live video feed, processes facial landmarks in real-time, and translates ocular coordinates into precise screen pixel movements.

✨ Key Features
1. High-Precision Eye Tracking
Utilizing the MediaPipe Face Mesh, the system tracks 468+ facial landmarks. It specifically isolates the iris and eyelid regions to ensure that the cursor follows the user's gaze with minimal jitter.

2. Gesture-Based Clicking
Standard mouse functions are replaced by facial gestures:

Left Click: Triggered by a deliberate blink of the left eye.

Right Click: Triggered by a deliberate blink of the right eye.

Double Click: Managed through specific blink duration thresholds.

3. Adaptive Smoothing
To prevent the cursor from "shaking" due to natural eye micro-movements, the project implements a Linear Interpolation (Lerp) or Moving Average algorithm. This ensures that the cursor movement feels fluid and professional, similar to a physical mouse.

4. Zero-Hardware Requirement
Unlike expensive eye-tracking hardware (like Tobii), this software requires nothing more than a standard 720p built-in laptop webcam.

🛠️ Technical Architecture & Stack
The project is built on a modular Python architecture, ensuring that the processing pipeline is efficient enough to run on standard CPUs without requiring a dedicated GPU.

Language: Python 3.10+

Computer Vision: OpenCV is used for capturing video frames and rendering the debugging overlay.

AI Inference: MediaPipe (by Google) is used for its lightweight, high-performance face mesh solution.

System Automation: PyAutoGUI handles the low-level OS instructions to move the cursor and execute click events.

Mathematical Operations: NumPy is used to calculate the Eye Aspect Ratio (EAR) and coordinate mapping.

🚀 Installation & Setup
Follow these steps to get the environment ready on your local machine:

1. Clone the Repository
Bash
git clone https://github.com/your-username/eye-mouse-tracker.git
cd eye-mouse-tracker
2. Environment Configuration
It is recommended to use a virtual environment to avoid dependency conflicts:

Bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Dependency Installation
Install the necessary libraries using the following command:

Bash
pip install opencv-python mediapipe pyautogui
4. Running the Application
Ensure your webcam is not being used by another app (like Zoom or Teams) and run:

Bash
python main.py
🔍 How It Works: The Science Behind the Code
The application follows a four-stage pipeline:

Frame Capture: The webcam captures frames at 30-60 FPS.

Landmark Detection: MediaPipe identifies the specific indices for the upper and lower eyelids.

EAR Calculation: The Eye Aspect Ratio (EAR) is calculated using the Euclidean distance between eyelid landmarks. If the ratio falls below a certain threshold (e.g., 0.2), a "Blink" is detected.

Coordinate Mapping: The normalized coordinates of the eye (0.0 to 1.0) are mapped to the user's screen resolution (e.g., 1920x1080) using the pyautogui.moveTo() function.

🚧 Challenges & Troubleshooting
Low Lighting: The system may struggle in dark environments. For best results, ensure your face is well-lit.

Screen Scaling: On some Windows machines, screen scaling (125% or 150%) can cause the cursor to stay in one corner. This can be fixed by disabling "Display Scaling" in the script.

CPU Usage: If the lag is high, try reducing the frame resolution in the OpenCV settings to 640x480.
