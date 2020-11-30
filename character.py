from cmu_112_graphics import *
import minions
import copy
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
        self.price=160
        self.direction="front"
        self.placed=False
        self.isValid=False
    def shoot(self,L,P):
        a=L+P
        for i in a:
            d= distance(self.cx,self.cy,i.cx,i.cy)
            if d < self.range*50:
                i.health-=self.attack
                if i.cx>self.cx and  i.cy>self.cy :
                    self.direction="right"
                elif  i.cx<self.cx  and  i.cy>self.cy :
                    self.direction="left"
                else:
                    self.direction="back"
                return (i.cx,i.cy)

        

