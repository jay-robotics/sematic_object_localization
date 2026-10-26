# semantic_object_localization

A ROS 2 package that gives a TurtleBot3 (or a fleet of them) the ability to see, name, and remember where objects are. It fuses YOLO object detection from an onboard camera with 2D LiDAR to localize detected objects (chairs, tables, bottles, people, etc.) into real-world map coordinates, then lets you send the robot to any object by name — e.g. "go to the chair" — through a live web dashboard.

## Demo

[![Watch the demo](https://img.youtube.com/vi/CyFAF_46Zg8/maxresdefault.jpg)](https://youtu.be/CyFAF_46Zg8)

## My DIY TurtleBot

<p align="center">
  <img width="70%" alt="front" src="https://github.com/user-attachments/assets/af74a811-5fc8-496f-8e4e-a2a0e28bcad0" />
  <img width="70%" alt="side" src="https://github.com/user-attachments/assets/b89b84fe-370c-4311-8541-b0b16f54ac22" />
  <img width="70%" alt="side2" src="https://github.com/user-attachments/assets/9694ad78-e866-4807-b734-111e5fe8ed54" />
  <img width="70%" alt="back" src="https://github.com/user-attachments/assets/4f439928-50c0-4767-a224-44b347462360" />
  <img width="70%" alt="above" src="https://github.com/user-attachments/assets/d60ee4f6-c0de-446b-9f55-3a549678e082" />
</p>

## Overview

Each robot runs a synchronized camera + LiDAR pipeline:

- **Detect** — YOLO (`yolo11x`) runs on the live camera feed to detect and classify objects in view.
- **Localize** — the detected object's horizontal position in the image is mapped to the matching LiDAR ray to estimate its distance, then that point is transformed through TF2 from the robot's sensor frame into the shared `world` map frame.
- **Remember** — each object's world coordinates are stored in a semantic map (a name → coordinates lookup), so the robot builds up a memory of what it has seen and where.
- **Navigate** — a web dashboard (built with `roslib.js` + ROSBridge) lists all discovered objects; picking one sends a Nav2 goal straight to that object's location, with live distance/ETA feedback.
- **Share** — in multi-robot setups, each robot broadcasts its detections over a shared topic, so every robot's semantic map builds from what the whole fleet has seen, not just its own camera.

## Tech

ROS 2 · Python (`rclpy`) · YOLO (Ultralytics) · OpenCV · `cv_bridge` · TF2 · Nav2 (`nav2_simple_commander`) · `message_filters` (camera-LiDAR sync) · custom ROS message (`ObjectDetectionShare`) · roslib.js / ROSBridge web dashboard

## License

Apache-2.0
