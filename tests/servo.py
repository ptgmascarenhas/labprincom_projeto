class Servo():
    def __init__(self):
        self.angle = 0
    
    def move(self):
        self.angle = self.angle + 1
        if (self.angle > 180):
            self.angle = 0

        return self.angle