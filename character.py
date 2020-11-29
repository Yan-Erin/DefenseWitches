from cmu_112_graphics import *
import minions
import mapDraw

def distance(x,y,x1,y1):
    return ((x1-x)**2 +(y1-y)**2)**0.5
class Daisy(object):
    def __init__(self,x,y):
        self.cx=x
        self.cy=y
        self.attack=2
        self.speed=2
        self.range=2
        self.i=0
        self.direction="front"
        self.placed=False
    def shoot(self):
        for i in mapDraw.app.minionList:
            distance= distance(self.cx,self.cy,i.cx,i.cy)
            if distance< self.range*50:
                i.health-=2
                return (i.cx,i.cy)

        

