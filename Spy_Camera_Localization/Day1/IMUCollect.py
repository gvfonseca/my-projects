from sense_hat import SenseHat
import numpy as np
import time
import scipy.signal as signal
from datetime import datetime,date
import matplotlib.pyplot as plt
import pandas as pd
import csv
import scipy.integrate as integrate
path="/home/pi/lab3/" # Change the path to your current folder (you can use `pwd` command in terminal to find the full path)
sense=SenseHat()



timestamp_fname=datetime.now().strftime("%H:%M:%S")
sense.set_imu_config(True,True,True) ## Config the Gyroscope, Accelerometer, Magnetometer
filename="datapath_midterm.csv"
header = ["timestamp,time,x_a,y_a,z_a,x_m,y_m,z_m,x_g,y_g,z_g"]
header_set = ["timestamp","time","x_a","y_a","z_a","x_m","y_m","z_m","x_g","y_g","z_g"]
with open(filename,"w") as f:
    print("collecting data now")
    writer = csv.writer(f)
    writer.writerow(header_set)
    while True:
        accel=sense.get_accelerometer_raw()  ## returns float values representing acceleration intensity in Gs
        orient=sense.get_orientation_radians()  ## returns float values representing rotation of the axis in radians
        mag=sense.get_compass_raw()  ## returns float values representing magnetic intensity of the ais in microTeslas
        gyro=sense.get_gyroscope_raw()
    
        x=accel['x']
        y=accel['y']
        z=accel['z']
        gyro_x=gyro['x']
        gyro_y=gyro['y']
        gyro_z=gyro['z']
        timestamp=datetime.now().strftime("%H:%M:%S")
        entry= str(time.time())+","+timestamp+","+str(x)+","+str(y)+","+str(z)+","+ str(mag['x'])+ ","+str(mag['y'])+","+ str(mag['z'])+","+str(gyro_x)+","+str(gyro_y)+","+str(gyro_z)+"\n"
    
    

        
        f.write(entry)
   
        
f.close()
        



