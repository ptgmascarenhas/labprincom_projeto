from time import sleep
from hc_sr04 import HC_SR04
from servo import Servo

sensor = HC_SR04()
servo = Servo()

mapa = []

for i in range(0, 90):
    servo.set_angle(i)
    dst = sensor.get_distance()
    medida = {"angle": i; "distance":dst}
    mapa = mapa.append{medida}

print(mapa)