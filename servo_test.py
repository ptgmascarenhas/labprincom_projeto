from servo import Servo

device = Servo()

try:
  while True:
    device.angle = input("Digite um angulo destino ")
    device.set_angle()

except KeyboardInterrupt:
  GPIO.cleanup()
