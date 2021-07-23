#!/usr/bin/env python
import RPi.GPIO as GPIO
import subprocess
import time


#add this to crontab @reboot sudo python /home/pi/listen_for_shutdown.py > /dev/null 2>&1
GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.wait_for_edge(3, GPIO.RISING)
#subprocess.call(['shutdown', '-h', 'now'], shell=False)
while GPIO.input(3) == GPIO.LOW:
    time.sleep(0.5)
subprocess.call(['shutdown', '-h', 'now'], shell=False)
