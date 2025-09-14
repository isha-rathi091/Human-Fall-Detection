# Human Fall Detection System

## Overview
Real-time fall detection using CNNs and video surveillance. Sends SMS and buzzer alerts when a fall or abnormal vital is detected. Designed for Raspberry Pi with optional heartbeat sensor.

## Features
- CNN-based fall detection (93.98% accuracy)
- Live video monitoring with OpenCV
- SMS alerts via Twilio
- Buzzer alerts for immediate notification
- Heartbeat sensor integration

## Installation
1. Clone the repo:
```bash
git clone https://github.com/your-username/human-fall-detection.git
cd human-fall-detection
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Add your trained CNN model to `models/fall_detection_model.h5`.
4. Configure Twilio credentials in `sms_alert.py`.

## Usage
```bash
python fall_detection.py
```
Press `q` to quit.

## Hardware Setup
- Raspberry Pi camera or USB camera
- Heartbeat sensor connected to ADC
- Buzzer on GPIO pin 18

