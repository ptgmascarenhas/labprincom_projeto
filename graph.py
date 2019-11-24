import numpy as np
import matplotlib.pyplot as plt
import random
from operator import itemgetter 

mapa = []

for i in range(0, 180):
    dst = random.randint(0, 300)
    medida = {'angle': i*np.pi/180, 'distance': dst}
    mapa.append(medida)

theta = list(map(itemgetter('angle'), mapa))
theta = [x-np.pi/2 for x in theta]
distance = list(map(itemgetter('distance'), mapa))

ax = plt.subplot(111, projection='polar')
ax.plot(theta, distance)
ax.set_rmax(300)
ax.set_rlabel_position(0)
ax.grid(True)
ax.set_thetamin(-90)
ax.set_thetamax(90)

plt.show()