# Spy Camera Localization

This project focuses on localizing a hidden camera or transmitter within a specified area using a combination of **Inertial Measurement Unit (IMU)** data and **Received Signal Strength Indicator (RSSI)** values. By integrating movement tracking and signal strength analysis, this project aims to accurately estimate the transmitter's position.

This project was created for a competition for CS 437 at UIUC, in which we were tasked with finding a hidden camera. In the first day, the camera was constantly transmitting packets, and in the second day the camera would only send data when motion was detected.

## Objectives

- Localize a hidden camera using RSSI and IMU data.
- Develop and implement a pipeline for step detection, trajectory plotting, and signal analysis.
- Evaluate performance over multiple tests to refine the localization strategy.

## System Overview

### Data Collection
- **IMU Data**: Captures accelerometer and gyroscope readings to determine steps and walking direction.
- **RSSI Data**: Records signal strength values from the camera for position estimation.

### Key Components
1. **Preprocessing**:
   - Data calibration to eliminate noise.
   - Step detection using smoothed acceleration peaks.
2. **IMU and RSSI Data Merging**:
   - Synchronization based on timestamps.
   - Filling gaps in RSSI data with the most recent value.
3. **Walking Strategy**:
   - Planned walking paths to maximize area coverage.
   - Real-time RSSI feedback through LED indicators.
4. **Localization Algorithm**:
   - Combine step detection and walking direction to create a trajectory.
   - Generate 2D heatmaps for refined position estimation.
5. **Post-Processing**:
   - Adjust trajectory plots for accuracy using step scaling and angle rounding.
   - Interpolate RSSI data for better precision.

## Results

### Day 1
- Challenges:
  - Inaccurate trajectory scaling led to incorrect localization.
  - Strong RSSI values in the wrong zone caused misleading estimates.
- Outcome: Estimated the camera in the wrong zone.

### Day 2
- Improvements:
  - Dynamic step scaling improved trajectory accuracy.
  - Correct localization achieved using heatmap interpolation and refined strategies.
- Outcome: Successfully localized the camera in the correct zone. Got third place for this day's results.

## Key Findings

1. **Step Length Variations**: Assuming constant step length is impractical; step scaling significantly improves accuracy.
2. **RSSI Analysis**: Outlier handling is essential to avoid misleading strong signal values.
3. **Trajectory and Heatmap Synergy**: Combining trajectory plots with interpolated heatmaps enhances localization accuracy.

## Tools and Technologies Used

- **Hardware**: Raspberry Pi with SenseHat, IMU sensors.
- **Data Processing**: Savitzky-Golay filters, signal integration, CSV merging.
- **Programming**: Python for data processing and visualization.

## Learning Outcomes

- Developed an integrated system for sensor-based localization.
- Improved signal analysis and trajectory plotting techniques.
- Refined strategies for real-time decision-making in constrained environments.

## Installation
May need to intall packages such as pandas.

Any package needed to be installed can be done simply by

pip install (package name)

Also, for the IMU_StepDetect_DAY1 and IMU_StepDetect_DAY2 python files, make sure the file path for the csv is correct.

### Usage
To run, you need to simultanousely run both the IMUCollect.py, and the collect_rssi_DAY1 or 2.py files.

Day 1:

In two seperate terminals, run:

sudo python3 IMUCollect.py
sudo python3 collect_rssi_DAY1.py

Then to analyze the resulted data, run 

IMU_StepDetect_DAY1.py

This will outputs relevant plots to track trajetcory and make a guess of location of camera.

Day 2:

In two seperate terminals, run:

sudo python3 IMUCollect_DAY2.py
sudo python3 collect_rssi_DAY2.py

Then to analyze the resulted data, run 

IMU_StepDetect_DAY2.py

This will outputs relevant plots to track trajetcory and make a guess of location of camera.

## Authors

Code was created primarily by Gustavo Fonseca and Anshul Kaushik with code inspired by CS 437 labs.
