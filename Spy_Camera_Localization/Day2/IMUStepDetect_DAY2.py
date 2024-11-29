import numpy as np
import time
import scipy.signal as signal
from datetime import datetime,date
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns # visualization
from scipy.interpolate import griddata
import math

filename="/home/pi/lab3/datapath_midterm_day2.csv"
rssi_filename = "/home/pi/lab3/rssi_midterm_day2.csv"
#joy_filename = "/home/pi/lab3/joystick_midterm_day2.csv"

## CSV file template:
# time in seconds, timestamp (H:M:S), X-Acceleration, Y-Acceleration, Z-Acceleration, X-Gyroscope,Y-Gyro,Z-Gyro,X-Gyro, Y-Gyro, Z-gyro


#joy = pd.read_csv(joy_filename,index_col = None)
df =pd.read_csv(filename, index_col=None)
print(df.head())
rssi_data =pd.read_csv(rssi_filename, index_col=None)
print(rssi_data.head())

merged_data = pd.merge_asof(df, rssi_data, on='timestamp', direction='nearest')
merged_data['rssi'].fillna(method='ffill', inplace=True)
merged_data.head()
#times_rssi = rssi_data['timestamp']
rssi_values = merged_data['rssi']

timestamp = merged_data['timestamp']
x_axis=merged_data['x_a']
y_axis=merged_data['y_a']
z_axis=merged_data['z_a']
yaw = merged_data['z_g']

print(len(x_axis))
## Visualize your Accelerometer Values
plt.plot(x_axis)
plt.plot(y_axis)
plt.plot(z_axis)
plt.show()



## CALIBERATION
# caliberate x,y,z to reduce the bias in accelerometer readings. Subtracting it from the mean means that in the absence of motion, the accelerometer reading is centered around zero to reduce the effect of integrigation drift or error.
# change the upper and lower bounds for computing the mean where the RPi is in static position at the begining of the experiment

lower, upper = 12, 25

x_calib_mean = np.mean(x_axis[lower:upper])
x_calib = x_axis - x_calib_mean


y_calib_mean = np.mean(y_axis[lower:upper])
y_calib = y_axis - y_calib_mean

z_calib_mean = np.mean(z_axis[lower:upper])
z_calib = z_axis - z_calib_mean
yaw_calib_mean = np.mean(yaw[lower:upper])
yaw_calib = (yaw - yaw_calib_mean)
yaw_calib = yaw_calib[:]
dt = [0]
for i in range(len(timestamp)-1):
    dt.append(timestamp[i+1] - timestamp[i])
def riemann(x,y):
    cumulative_sum = np.zeros(len(y))
    cumulative_sum[0] = 0
    dx = x[1] - x[0]
    for i in range(len(x) - 1):
      
        cumulative_sum[i+1] = cumulative_sum[i] + (y[i+1])*dx
    return cumulative_sum
riemann_result_yaw = riemann(dt,yaw_calib)
riemann_rounded = np.zeros_like(riemann_result_yaw)
for idx, x in enumerate(riemann_result_yaw):
    x = x/(np.pi/2)
    if idx > 260 and idx < 380:
        if x < 0:
            riemann_rounded[idx] = (np.pi/2)*(math.floor(x) if x - math.ceil(x) <= -0.35 else math.ceil(x))
        else:
            riemann_rounded[idx] = (np.pi/2)*(math.ceil(x) if x - math.floor(x) >= 0.35 else math.floor(x))
    else:
        
        if x < 0:
            riemann_rounded[idx] = (np.pi/2)*(math.floor(x) if x - math.ceil(x) <= -0.35 else math.ceil(x))
        else:
            riemann_rounded[idx] = (np.pi/2)*(math.ceil(x) if x - math.floor(x) >= 0.35 else math.floor(x))
#riemann_result_yaw = np.ceil(riemann_result_yaw/(np.pi/2))* (np.pi/2)
riemann_result_yaw = riemann_rounded
accel = signal.savgol_filter(z_calib, 21,2) # Enter function here to smooth z-axis acceleration, https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.savgol_filter.html
## Same as rolling average --> Savitzky-Golay smoothing
## change the window size as it seems fit. If you keep window size too high it will not capture the relevant peaks/steps
#riemann_result_yaw = signal.savgol_filter(riemann_result_yaw, 21,2)
# Plot the original and smoothed data
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(z_calib)
plt.title("Original Data")
plt.subplot(2, 1, 2)
plt.plot(accel)
plt.plot(riemann_result_yaw)
plt.title("Smoothed Data")
plt.show()


## Step Detection: The instantaneous peaks in the accelerometer readings correspond to the steps. We use thresholding technique to decide the range of peak values for step detection
# Set a minimum threshold (e.g., 1.0) for peak detection

min_threshold = 0.01  ## Change the threshold based on the peak accelerometer values that you observe in your plot above

# Calculate the upper threshold for peak detection as the maximum value in the data
upper_threshold = np.max(accel)

# Define the range for peak detection
my_range = (min_threshold, upper_threshold)

# print("range of Accel. values  for peak detection",my_range)
## Visualize the detected peaks in the accelerometer readings based on the selected range
plt.plot(timestamp, accel)

#Use this link to find the peaks: https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.find_peaks.html
peak_array, _ = signal.find_peaks(accel, height = min_threshold, distance = 3) # Enter function here

plt.plot(timestamp[peak_array], accel[peak_array], "x", color="r")
for i, peak in enumerate(peak_array):
    plt.text(timestamp[peak], accel[peak], f'{i + 1}', fontsize = 9, ha = 'left', va = 'bottom')
plt.ylabel("Accel (m/s^2)")
plt.xlabel("Time (s)")
plt.title("Smoothed Data")
plt.show()
#riemann_result_yaw = riemann_result_yaw[peak_array]
# Peak array indices -> peak_array
# Accel values at high peaks --> accel[peak_array]


# Set the orientation/direction of motion (walking direction).
# walking_direction is an angle in degrees with global frame x-axis. It can be from 0 degrees to 360 degrees.
# for e.g. if walking direction is 90 degrees, user is walking in the positive y-axis direction.
# Assuming you are moving along the +X-axis with minor deviations/drifts in Y, we set the orientation to 5 (ideally it should be 0 but to take into account the drifts we keep 5)

# Integrate the orientation data to get the walking direction
walking_dir = riemann_result_yaw ## deg to radi
# To compute the step length, we estimate it to be propertional to the height of the user.

height= 1.9 # in meters # Change the height of the user as needed
step_length= 0.8  # in meters

# Convert walking direction into a 2D unit vector representing motion in X, Y axis:
angle = np.array([np.cos(walking_dir), -np.sin(walking_dir)/.75])

## Start position of the user i.e. (0,0)
cur_position = np.array([0.0, 0.0], dtype=float)
t = []
print(len(riemann_result_yaw))
for i in range(len(riemann_result_yaw)):
    step_calib = 1
    if i in peak_array:
        if i<210:
            step_calib = 1.25
        if i>210 and i<320:
            step_calib = 0.76
        if i>320 and i<395:
            step_calib = 0.45
        if i>395 and i<490:
            step_calib =1.28
        if i>490 and i<600:
            step_calib = 1.44
        if i > 600:
            step_calib = 3
        cur_position = cur_position + step_length * angle[:,i] / (step_calib * 2)
    t.append(cur_position)
print(cur_position)
# Trajectory positions are stored in t, plot it for the submission with good plot labels as specified in the lab manual
t0 = [row[0] for row in t]

t1 = [row[1] for row in t]

print(len(t0))

#close_index = (merged_data['timestamp']- joy['timestamp'][0]).abs().idxmin()
#xy = t0[close_index]
#yy = t1[close_index]
max_avg = -100000
max_pos = 0
for i in range(len(rssi_values) - 10):
    temp_avg = rssi_values[i] + rssi_values[i+1] + rssi_values[i+2] + rssi_values[i+3] + rssi_values[i+4] + rssi_values[i+5] + rssi_values[i+6] + rssi_values[i+7] +rssi_values[i+8] + rssi_values[i+9]
    temp_avg = temp_avg/10
    if(temp_avg > max_avg):
        max_avg = temp_avg
        max_pos = i+5
t0 = np.array(t0)
t1 = np.array(t1)
xy_avg = t0[max_pos]
yy_avg = t1[max_pos]
time_avg = timestamp[max_pos] -timestamp[0]
print("Timestampe: " + str(time_avg))
plt.scatter(t0,t1, c=rssi_values, cmap='viridis', s=100)
#plt.scatter(xy,yy,c='red',marker='x')
plt.scatter(xy_avg,yy_avg,c='blue',marker='+')
plt.title("Trajectory with RSSI")
plt.colorbar(label='Signal Strength (RSSI)')
plt.ylabel("Y position")
plt.xlabel("X position")
plt.show()
print(type(t0))
grid_x, grid_y = np.mgrid[t0.min():t0.max():1000j,t1.min():t1.max():1000j]
grid_rssi = griddata((t0,t1), rssi_values, (grid_x, grid_y), method='linear',fill_value = -62)
max_rssi_idx = np.unravel_index(np.argmax(grid_rssi,axis=None), grid_rssi.shape)
print(max_rssi_idx)
plt.imshow(grid_rssi.T, extent=(np.min(t0),np.max(t0),np.min(t1),np.max(t1)), origin='lower', cmap='viridis')
plt.plot(grid_x[max_rssi_idx]/2,grid_y[max_rssi_idx]/2,'ro',label = "MAX") 
plt.colorbar(label='Signal Strength (RSSI)')
plt.title("RSSI HeatMap")
plt.ylabel("Y position")
plt.xlabel("X position")
plt.show()