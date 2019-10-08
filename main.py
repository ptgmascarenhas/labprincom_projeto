import RPi.GPIO as GPIO
from HC_SR04 import HC_SR04
import time

GPIO.setmode(GPIO.BCM)

sensor = HC_SR04()

sensor.get_distance()

GPIO.cleanup()
