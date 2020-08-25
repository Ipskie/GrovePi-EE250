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

ULTRASONIC_PORT = 8 # D8
ROTARY_PORT = 7     # D7

# LCD Goes on I2C-1
LED_PORT = 3        # D7

grovepi.pinMode(LED_PORT, "OUTPUT")

if __name__ == '__main__':
    while True:
        # So we do not poll the sensors too quickly which may introduce noise,
        # sleep for a reasonable time of 200ms between each iteration.
        time.sleep(0.2)

        print(grovepi.ultrasonicRead(ULTRASONIC_PORT))
