
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

import struct


basesotation = Motor(Port.A)
firstarm1 = Motor(Port.B)

right_stick_x = 124
right_stick_y = 124
left_stick_x = 124
left_stick_y = 124


def scale(val, src, dst):
    """
    Scale the given value from the scale of src to the scale of dst.
 
    val: float or int
    src: tuple
    dst: tuple
 
    example: print(scale(99, (0.0, 99.0), (-1.0, +1.0)))
    """
    return (float(val - src[0]) / (src[1] - src[0])) * (dst[1] - dst[0]) + dst[0]



infile_path = "/dev/input/event4"


in_file = open(infile_path, "rb")


FORMAT = 'llHHI'    
EVENT_SIZE = struct.calcsize(FORMAT)
event = in_file.read(EVENT_SIZE)

while event:
    (tv_sec, tv_usec, ev_type, code, value) = struct.unpack(FORMAT, event)
    if ev_type == 3 and code == 3:
        right_stick_x = value
    if ev_type == 3 and code == 4:
        right_stick_y = value
    if ev_type == 3 and code == 0:
        left_stick_x = value
    if ev_type == 3 and code == 1:
        left_stick_y = value

    
    up = scale(right_stick_y, (0,255), (100,-100))
    left = scale(right_stick_x, (0,255), (100,-100))
    upl = scale(left_stick_y, (0,255), (100,-100))
    leftl = scale(left_stick_x, (0,255), (100,-100))
 
    basesotation.dc(left*0.75)
    secondarm.dc(upl*0.75)
    firstarm1.dc(-up*0.5)
    firstarm2.dc(-up*0.5)

 
    event = in_file.read(EVENT_SIZE)

in_file.close() 