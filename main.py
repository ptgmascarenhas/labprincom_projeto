import RPi.GPIO as GPIO
import HC_SR04
import time


sensor = HC_SR04()

sensor.get_distance()
