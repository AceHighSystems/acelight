
import can
import acelight
from acelight.modules import ranger_mk1_param as r 


CHANNEL = "/dev/cu.usbmodem2080317458421"  # Replace with your adapter's serial port.
BITRATE = 1_000_000
HOST_ID = 1
NODE_ID = 2

with can.Bus(interface="slcan", 
            channel=CHANNEL, 
            bitrate=BITRATE) as bus:

    ace = acelight.Client(HOST_ID, bus)

    status = ace.write(NODE_ID, r.profile_velocity, 10000) # set steps/second 
    print(f"Write status: 0x{status:02X}") # status code 0x01 means write was accepted by the module.

    for i in range(5):
        status, temperature = ace.read(NODE_ID, r.temperature) # update steps/sec
        print(f"Read status: 0x{status:02X}") # status code 0x02 means payload data follows
        print(f"Temperature data: {temperature/1000}")