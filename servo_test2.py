import RPi.GPIO as GPIO
import time

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(0) # Initialization
i = 1.5

try:
  while True:
    while True:
        p.ChangeDutyCycle(i)
        time.sleep(0.05)
#        print(i)
        i = round(i + 0.1, 1)
        if i >= 12.5:
            break
    while True:
        p.ChangeDutyCycle(i)
        time.sleep(0.05)
#        print(i)
        i = round(i - 0.1, 1)
        if i <= 1.5:
            break




except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()
