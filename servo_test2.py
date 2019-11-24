import RPi.GPIO as GPIO
from servo import Servo
import time

device = Servo()

try:
  while True:
    device.move()
    time.sleep(0.1)
    
except KeyboardInterrupt:
  GPIO.cleanup()
