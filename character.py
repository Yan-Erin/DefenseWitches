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
        self.clicked=False
        self.attackmethod=True
    def shoot(self,L,P):
        a=L+P
        if self.attackmethod==False:
            a=a[::-1]
        else:
            a=L+P
        for i in a:
            d= distance(self.cx,self.cy,i.cx,i.cy)
            if d < self.range*50:
                i.health-=self.attack
                if   i.cy<self.cy and i.cx>self.cx+5:
                    self.direction="back right"
                elif i.cy<self.cy and i.cx<self.cx+5:
                    self.direction="back left"
                elif i.cx>self.cx+5 and  i.cy>self.cy :
                    self.direction="right"
                elif  i.cx<self.cx-5  and  i.cy>self.cy :
                    self.direction="left"
                else:
                    self.direction="front"
                return (i.cx,i.cy)
    def upgrade(self):
        self.range+=0.5
        self.attack=2.5
class Chloe(Daisy):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.attack=1
        self.speed=1
        self.range=1.5
        self.price=240
    def shoot(self,L,P):
        a=L+P
        bo=False
        for i in a:
            d= distance(self.cx,self.cy,i.cx,i.cy)
            if d < self.range*50:
                bo=True
                i.health-=self.attack
        return bo
        

