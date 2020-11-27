from cmu_112_graphics import *
import minions

class Daisy(object):
    def __init__(self,x,y):
        self.cx=x
        self.cy=y
        self.attack=2
        self.speed=2
        self.range=1
        self.i=0
        self.direction="front"

    def timerFired(self):
        self.i+=1
            
    def redrawAll(self,canvas):
        Daisy.daisyAttack(self,canvas,self.direction)
