from time import sleep
from hc_sr04 import HC_SR04
from servo import Servo

sensor = HC_SR04()
servo = Servo()

mapa = []

for i in range(0, 180):
    servo.angle = i
    servo.set_angle()
    sleep(0.05)
    dst = sensor.get_distance()
    medida = {'angle': i, 'distance':round(dst,2)}
    mapa.append(medida)

print(mapa)