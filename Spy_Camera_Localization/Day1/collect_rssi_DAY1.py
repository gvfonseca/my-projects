import csv
from datetime import datetime
from scapy.all import *
import time
import asyncio
from sense_hat import SenseHat
import time
sense = SenseHat()
sense.clear()
"""
Run monitor_mode.sh first to set up the network adapter to monitor mode and to
set the interface to the right channel.
To get RSSI values, we need the MAC Address of the connection 
of the device sending the packets.
"""

# Variables to be modified
#dev_mac = "e4:5f:01:d4:9f:f9"  # Change to a hidden camera's MAC
dev_mac_test = "e4:5f:01:d4:a0:6b"
dev_mac = "d8:3a:dd:2f:4c:cc"
iface_n = "wlan1"  # Interface for network adapter (do not modify)
duration = 120  # Number of seconds to sniff for
rssi_file_name = "rssi_midterm.csv"  # Output RSSI CSV file name
joystick_file_name = "joystick_midterm.csv"  # Output joystick CSV file name

q_rssi = []  # Queue for RSSI values

is_pressed = False
def create_rssi_file():
    """Create and prepare a file for RSSI values"""
    header = ["timestamp", "dest", "src", "rssi"]
    with open(rssi_file_name, "w", encoding="UTF8") as f:
        writer = csv.writer(f)
        writer.writerow(header)

def create_joystick_file():
    """Create and prepare a file for joystick input"""
    header = ["timestamp", "key"]
    with open(joystick_file_name, "w", encoding="UTF8") as f:
        writer = csv.writer(f)
        writer.writerow(header)

def write_to_file(file_name, data):
    """Write data to a file"""
    with open(file_name, "a", encoding="UTF8") as f:
        writer = csv.writer(f)
        writer.writerow(data)


def captured_packet_callback(pkt):
    """Save MAC addresses, time, and RSSI values to CSV file if MAC address of src matches.
    
    Example output CSV line:
    2024/02/11,11:12:13.12345, 1707692954.1, 00-B0-D0-63-C2-26, 00:00:5e:00:53:af, -32.2
    """
    cur_dict = {}
    # Check pkt for dst, src, and RSSI field
    try:
        cur_dict["mac_1"] = pkt.addr1
        cur_dict["mac_2"] = pkt.addr2
        cur_dict["rssi"] = pkt.dBm_AntSignal
        print(cur_dict)
    except AttributeError:
        return  # Ignore packet without RSSI field

    # date_time = datetime.now().strftime("%d/%m/%Y,%H:%M:%S.%f")  # Get current datetime
    timestamp = time.time()
    send = False
    # @TODO: Filter packets with src = the hidden camera's MAC
    if pkt.addr2 == dev_mac:
        write_to_file("rssi_midterm.csv", [timestamp,pkt.addr1,pkt.addr2, pkt.dBm_AntSignal])
        q_rssi.append(pkt.dBm_AntSignal)
        #sense.set_pixel(3,3,(124,156,125))
        #sense.set_pixel(3,4,(26,36,23))
        #sense.set_pixel(4,3,(24,200,35))
        #sense.set_pixel(4,4,(178,178,156))
        average_rssi = pkt.dBm_AntSignal
        if(len(q_rssi) > 5):
            rssi_ten = q_rssi[-5:]
            average_rssi = sum(rssi_ten)/len(rssi_ten)

        if (average_rssi > -45):
            for x in range(2):
                for y in range(8):
                    sense.set_pixel(x, y, (255, 0, 0))  # Yellow
            for x in range(2):
                for y in range(8):
                    sense.set_pixel(x+2, y, (255, 255, 0))    # Red
            for x in range(2):
                for y in range(8):
                    sense.set_pixel(x+4, y, (0, 255, 0))    # Red
            for x in range(2):
                for y in range(8):
                    sense.set_pixel(x+6, y, (0, 0, 255))    # Red
        elif (average_rssi > -47.5):
            for x in range(2):
                for y in range(8):
                    sense.set_pixel(x, y, (255, 0, 0))  # Yellow
            for x in range(2):
                for y in range(8):
                    sense.set_pixel(x+2, y, (255, 255, 0))    # Red
            for x in range(2):
                for y in range(8):
                    sense.set_pixel(x+4, y, (0, 255, 0))    # Red
            for x in range(1):
                for y in range(8):
                    sense.set_pixel(x+6, y, (0, 0, 255))
                    sense.set_pixel(x+7, y, (0, 0, 0))# Red
        elif (average_rssi > -50):
            for x in range(2):
                for y in range(8):
                    sense.set_pixel(x, y, (255, 0, 0))  # Yellow
            for x in range(2):
                for y in range(8):
                    sense.set_pixel(x+2, y, (255, 255, 0))    # Red
            for x in range(2):
                for y in range(8):
                    sense.set_pixel(x+4, y, (0, 255, 0))    # Red
            for x in range(2):
                for y in range(8):
                    sense.set_pixel(x+6, y, (0, 0, 0))# Red
        elif (average_rssi > -52.5):
            for x in range(2):
                for y in range(8):
                    sense.set_pixel(x, y, (255, 0, 0))  # Yellow
            for x in range(2):
                for y in range(8):
                    sense.set_pixel(x+2, y, (255, 255, 0))    # Red
            for x in range(1):
                for y in range(8):
                    sense.set_pixel(x+4, y, (0, 255, 0))    # Red
                    sense.set_pixel(x+5, y, (0, 0, 0))
            for x in range(2):
                for y in range(8):
                    sense.set_pixel(x+6, y, (0, 0, 0))# Red
        elif (average_rssi > -55):
            for x in range(2):
                for y in range(8):
                    sense.set_pixel(x, y, (255, 0, 0))  # Yellow
            for x in range(2):
                for y in range(8):
                    sense.set_pixel(x+2, y, (255, 255, 0))    # Red
            for x in range(2):
                for y in range(8):    # Red
                    sense.set_pixel(x+4, y, (0, 0, 0))
            for x in range(2):
                for y in range(8):
                    sense.set_pixel(x+6, y, (0, 0, 0))# Red
        elif (average_rssi > -57.5):
            for x in range(2):
                for y in range(8):
                    sense.set_pixel(x, y, (255, 0, 0))  # Yellow
            for x in range(1):
                for y in range(8):
                    sense.set_pixel(x+2, y, (255, 255, 0))    # Red
                    sense.set_pixel(x+3, y, (0, 0, 0)) 
            for x in range(2):
                for y in range(8):    # Red
                    sense.set_pixel(x+4, y, (0, 0, 0))
            for x in range(2):
                for y in range(8):
                    sense.set_pixel(x+6, y, (0, 0, 0))# Red
        elif (average_rssi > -59):
            for x in range(2):
                for y in range(8):
                    sense.set_pixel(x, y, (255, 0, 0))  # Yellow
            for x in range(1):
                for y in range(8):
                    sense.set_pixel(x+2, y, (0, 0, 0))    # Red
                    sense.set_pixel(x+3, y, (0, 0, 0)) 
            for x in range(2):
                for y in range(8):    # Red
                    sense.set_pixel(x+4, y, (0, 0, 0))
            for x in range(2):
                for y in range(8):
                    sense.set_pixel(x+6, y, (0, 0, 0))# Red
        elif (average_rssi > -61):
            for x in range(1):
                for y in range(8):
                    sense.set_pixel(x, y, (255, 0, 0))  # Yellow
                    sense.set_pixel(x+1, y, (0, 0, 0))
            for x in range(1):
                for y in range(8):
                    sense.set_pixel(x+2, y, (0, 0, 0))    # Red
                    sense.set_pixel(x+3, y, (0, 0, 0)) 
            for x in range(2):
                for y in range(8):    # Red
                    sense.set_pixel(x+4, y, (0, 0, 0))
            for x in range(2):
                for y in range(8):
                    sense.set_pixel(x+6, y, (0, 0, 0))# Red
        else:
            sense.clear()

    


async def record_joystick() -> str:
    """Record joystick input to CSV file"""
    events = sense.stick.get_events()
    for event in events:
        if (event.action == "pressed"):
            return True
    


async def main_loop():
    """Main loop to record joystick input and IMU data (in Lab 3)"""
    start = time.time()
    
    while (time.time() - start) < duration:
        # Record joystick input
        key_pressed = await record_joystick()
        if key_pressed:
            # Write (timestamp, key) to the CSV file
            write_to_file(joystick_file_name, [time.time(), key_pressed])

        # await display_rssi()
        


if __name__ == "__main__":
    create_rssi_file()
    create_joystick_file()

    start_date_time = datetime.now().strftime("%d/%m/%Y,%H:%M:%S.%f") #Get current date and time
    print("Start Time: ", start_date_time)

    t = AsyncSniffer(iface=iface_n, prn=captured_packet_callback, store=0)
    t.daemon = True
    t.start()    

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main_loop())
    loop.close()
    
    # @TODO: Start IMU data collection loop here
    ## Hint: in the loop, pop latest value from RSSI queue and put in CSV file if available, else write None or -100
    ### Hint: Use write_to_file(file_name, data) function to write a list of values to the CSV file
    sense.clear()
    t.stop()
