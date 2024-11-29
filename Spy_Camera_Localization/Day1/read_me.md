## Day 1 Setup

***This is for the first day where the camera constantly was sending packets.***

This repository contains code and plots used for each of the two days of the comptetion. You can run the code for data collections which will create new csv files to hold data. Next, you run the Step Detect python files which analyze the csv data and output trajectory plots with a guess as to where the camera location may be.


## Installation
May need to intall packages such as pandas.

Any package needed to be installed can be done simply by

pip install (package name)

## Usage
To run, you need to simultanousely run both the IMUCollect.py, and the collect_rssi_DAY1 or 2.py files.

Day 1:

In two seperate terminals, run:

sudo python3 IMUCollect.py
sudo python3 collect_rssi_DAY1.py

Then to analyze the resulted data, run 

IMU_StepDetect_DAY1.py

This will outputs relevant plots to track trajetcory and make a guess of location of camera.


## Collaborators

Code was created primarily by Anshul Kaushik and Gustavo Fonseca with some large chunks of code taken from given code for CS 437 Lab 3.