from time import sleep
import RPi.GPIO as GPIO
from hc_sr04 import HC_SR04

GPIO.setmode(GPIO.BCM)

sensor = HC_SR04()

try:
	while True:
		dst = sensor.get_distance()
		print(f'Distancia: {dst} cm')
		sleep(1)
				
except KeyboardInterrupt:
	GPIO.cleanup()