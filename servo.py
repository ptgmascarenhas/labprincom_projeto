import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

class Servo():
    def __init__(self):
        #set GPIO Pins
        self.servo_pin = 18
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

    def set_angle(self,angle):
        duty = self.deg_0_duty + (angle/180.0)* self.duty_range
        self.pwm.ChangeDutyCycle(duty)
    
    def move(self):
        return 0