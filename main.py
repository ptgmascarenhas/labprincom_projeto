import RPi.GPIO as GPIO
import ultrasonic_sensor
import time

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 24
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

try:
    while True:
        dist = ultrasonic_sensor.get_distance()
        print ("Measured Distance = %.1f cm" % dist)
        time.sleep(1)
 
except KeyboardInterrupt:
    print("Stoping...")
    GPIO.cleanup()