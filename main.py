import RPi.GPIO as GPIO
from hc_sr04 import HC_SR04
import time

GPIO.setmode(GPIO.BCM)

sensor = HC_SR04()

try:
    dst = sensor.get_distance()
    print(f'Distancia: {dst}')
except:
    print('Desligando')
    GPIO.cleanup()
