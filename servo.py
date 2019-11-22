import RPi.GPIO as GPIO
import time

class Servo():
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        self.position = 1
        self.lastangle = 0
        #set GPIO Pins
        self.angle = 0
        self.servo_pin = 17
        self.deg_0_pulse   = 0.5 
        self.deg_180_pulse = 2.5
        self.f = 50.0  
        # Faca alguns calculos dos parametros da largura do pulso
        self.period = 1000/self.f
        self.k      = 100/self.period
        self.deg_0_duty = self.deg_0_pulse*self.k
        self.pulse_range = self.deg_180_pulse - self.deg_0_pulse
        self.duty_range = self.pulse_range * self.k
        
        #Iniciar o pino gpio
        GPIO.setup(self.servo_pin,GPIO.OUT)
        self.pwm = GPIO.PWM(self.servo_pin,self.f)
        self.pwm.start(0)

    def set_angle(self):
        duty = self.deg_0_duty + (int(self.angle)/180.0)* self.duty_range
        self.pwm.ChangeDutyCycle(duty)
    
    def move(self):
        if self.position == 1:
            self.angle = self.lastangle + 1
            if self.angle > 90:
                self.position = -1

        if self.position == -1:
            self.angle = self.lastangle - 1
            if self.angle == 0:
                self.position = 1

        self.lastangle = self.angle

        
        self.set_angle()

        return self.angle
