import RPi.GPIO as GPIO
from hc_sr04 import HC_SR04
import time

GPIO.setmode(GPIO.BCM)

sensor = HC_SR04()

dst = sensor.get_distance()

GPIO.cleanup()
