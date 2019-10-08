import RPi.GPIO as GPIO
import ultrasonic_sensor
import time


try:
    while True:
        dist = ultrasonic_sensor.get_distance()
        print ("Measured Distance = %.1f cm" % dist)
        time.sleep(1)
 
except KeyboardInterrupt:
    print("Stoping...")
    GPIO.cleanup()
