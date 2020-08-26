""" EE 250L Lab 02: GrovePi Sensors

Elijah Yap  

https://github.com/Ipskie/GrovePi-EE250
"""

"""python3 interpreters in Ubuntu (and other linux distros) will look in a 
default set of directories for modules when a program tries to `import` one. 
Examples of some default directories are (but not limited to):
  /usr/lib/python3.5
  /usr/local/lib/python3.5/dist-packages

The `sys` module, however, is a builtin that is written in and compiled in C for
performance. Because of this, you will not find this in the default directories.
"""
# By appending the folder of all the GrovePi libraries to the system path here,
# we successfully `import grovepi`
import grovepi
import sys
import time
sys.path.append('../../Software/Python/')
# This append is to support importing the LCD library.
sys.path.append('../../Software/Python/grove_rgb_lcd')
from grove_rgb_lcd import *

ULTRASONIC_PORT = 8 # Digital Port D8
ROTARY_PORT = 0     # Anaolog Port A0

# LCD Goes on I2C-1
LED_PORT = 3        # Digital Port D7

grovepi.pinMode(LED_PORT, "OUTPUT")

# upper and lower bounds of potentiometer output
rotary_limits = (0, 1023)

# ROUGH upper and lower bounds of ranger output
ranger_limits = (0, 150)

if __name__ == '__main__':
    while True:
        # So we do not poll the sensors too quickly which may introduce noise,
        # sleep for a reasonable time of 200ms between each iteration.
        time.sleep(0.2)

        # get rotary value
        threshhold = grovepi.analogRead(ROTARY_PORT)
        
        # get range
        n_range = grovepi.ultrasonicRead(ULTRASONIC_PORT)

        OBJ_PRES = ""
        if n_range < threshhold:
            OBJ_PRES = "OBJ PRES"
            setRGB(128, 0, 0)
        else:
            setRGB(0, 128, 0)
        setText_norefresh(f"{threshhold:4}cm {OBJ_PRES}\n {n_range:3}cm")
