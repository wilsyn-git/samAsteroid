from circleshape import *

class Player(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        self.rotation = 0
        
