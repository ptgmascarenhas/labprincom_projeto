from time import sleep
from hc_sr04 import HC_SR04
from servo import Servo
import numpy as np
import matplotlib.pyplot as plt
import random
from operator import itemgetter 
import RPI.GPIO as GPIO

sensor = HC_SR04()
servo = Servo()

mapa = []

while servo.angle <= 180:
    ang = servo.move2()
    sleep(0.05)
    dst1 = sensor.get_distance()
    dst2 = sensor.get_distance()
    dst = (dst1+dst2)/2
    medida = {'angle': ang*np.pi/180, 'distance': dst}
    mapa.append(medida)

theta = list(map(itemgetter('angle'), mapa))
#theta = [x-np.pi/2 for x in theta]
distance = list(map(itemgetter('distance'), mapa))

graph = plt.subplot(111, projection='polar')
graph.plot(theta, distance)
graph.set_rmax(50)
graph.set_rmin(0)
graph.set_rticks([10, 20, 30, 40])
graph.set_rlabel_position(0)
graph.grid(True)
graph.set_thetamin(0)
graph.set_thetamax(180)


GPIO.cleanup()

plt.savefig('grafico.png')