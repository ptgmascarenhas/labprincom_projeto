import RPi.GPIO as GPIO
import time

class Servo():
	def __init__(self):
		GPIO.setmode(GPIO.BCM)
		self.pin = 17
		self.pwm_max = 11.5
		self.pwm_min = 2.5
		self.pwm_range = self.pwm_max - self.pwm_min
		self.frequency = 50
		self.duty_cycle = self.pwm_min
		self.angle = 0
		self.direction = 0
		GPIO.setup(self.pin, GPIO.OUT)
		self.pwm = GPIO.PWM(self.pin, self.frequency)
		self.pwm.start(0)
		
	def set_angle(self):		
		self.duty_cycle = self.pwm_min + self.pwm_range * (int(self.angle)/180.0)
		self.pwm.ChangeDutyCycle(self.duty_cycle)
		
	def move(self):
		if self.direction == 0: #indo de 0 -> 180
			self.angle = self.angle + 2
			self.duty_cycle = self.duty_cycle + 0.1
			if self.angle > 180:
				self.direction = 1
		
		if self.direction == 1: #voltando de 180 -> 0
			self.angle = self.angle - 2
			self.duty_cycle = self.duty_cycle - 0.1
			if self.angle < 0:
				self.direction = 0
				self.move()		
			
		self.pwm.ChangeDutyCycle(self.duty_cycle)
		return self.angle