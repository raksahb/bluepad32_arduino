from pybricks.hubs import TechnicHub
from pybricks.pupdevices import Motor
from pybricks.iodevices import PUPDevice
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
import ustruct

p=PUPDevice(Port.A)

def read_gamepad():
    a=p.read(0)
    outp=ustruct.unpack('6h',ustruct.pack('12b',*a))
    print(outp)
    return outp

def led(nr,r,g,b):
    p.write(0,(0,0,0,0,0,0,0,0,nr,r,g,b))
    read_gamepad()

def showled():
    p.write(0,(0,0,0,0,0,0,0,0,65,0,0,0))


while True:
    for l in range(6):
        for i in range(6):
            led(i,0,0,0)
            #wait(2)
        led(l,30,0,0)
        showled()
        wait(20)    
    for l in range(5,1,-1):
        for i in range(6):
            led(i,0,0,0)
            #wait(2)
        led(l,30,0,0)
        showled()
        wait(20)
