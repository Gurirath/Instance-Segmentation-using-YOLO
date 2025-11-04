# Interactive YOLOv8 Instance Segmentation Tracker

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)

A real-time object tracker using YOLOv8-seg that allows you to select an object, track it, and interactively edit its segmentation mask. The custom mask persists and moves with the object.



## Features

* **Real-time Tracking:** Uses YOLOv8 and ByteTrack to track multiple objects from a webcam feed.
* **Interactive Selection:** Click on any object to isolate and track it with a custom highlight color.
* **Persistent Mask Editing:**
    * Pause the feed to edit the segmentation mask of the selected object.
    * Paint with the Left Mouse Button to add to the mask.
    * Erase with the Right Mouse Button to remove from the mask.
    * Adjust brush size.
* **Dynamic Mask Translation:** The user-edited mask is saved and translated to follow the object as it moves.
* **GUI Controls:** A separate Tkinter window provides controls for switching cameras, adjusting colors, and managing tracking.

## Installation

1.  Clone the repository:
    ```bash
    git clone [https://github.com/Gurirath/Instance-Segmentation-using-YOLO.git](https://github.com/Gurirath/Instance-Segmentation-using-YOLO.git)
    cd Instance-Segmentation-using-YOLO
    ```

2.  Install the required Python libraries:
    ```bash
    pip install -r requirements.txt
    ```

    If you don't have a `requirements.txt` file, you can create one with the following content:
    ```text
    opencv-python-headless
    numpy
    ultralytics
    ```
    Then run `pip install -r requirements.txt`.

## Setup

This project requires the YOLOv8n segmentation model weights.

**Note:** The `.pt` model file should not be stored in Git. If you have already pushed it, please remove it and add `*.pt` to a `.gitignore` file.

You can download the required model file (`yolov8n-seg.pt`) from the Ultralytics assets.

```bash
# On Linux/macOS
wget [https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n-seg.pt](https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n-seg.pt)

# On Windows (PowerShell)
Invoke-WebRequest -Uri [https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n-seg.pt](https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n-seg.pt) -OutFile yolov8n-seg.pt
