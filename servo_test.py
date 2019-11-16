from servo import Servo

device = Servo()

while True:
    device.angle = input("Digite um angulo destino ")
    device.set_angle()
