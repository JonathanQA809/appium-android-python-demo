# Appium Android Python Demo

Mobile automation testing project using Python, Pytest, Appium, and Android Emulator.

## Tech Stack

- Python
- Pytest
- Appium
- Android Emulator
- UiAutomator2
- Appium Inspector

## Project Overview

This project automates Android Settings application testing using Appium and Python.

Automated test coverage includes:
- Verifying Settings app launches successfully
- Verifying Apps option is visible

## Project Structure

```text
appium-android-python-demo/
├── test_settings_app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Setup Instructions

### Clone Repository

```bash
git clone https://github.com/JonathanQA809/appium-android-python-demo.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Start Android Emulator

```bash
adb devices
```

### Start Appium Server

```bash
appium
```

### Run Tests

```bash
pytest -v
```

## Test Results

```text
2 passed
```

## Skills Demonstrated

- Mobile Automation Testing
- Android Emulator Configuration
- Appium Setup
- Python Test Automation
- Pytest Framework
- Element Inspection with Appium Inspector
- Android Device Connection using adb