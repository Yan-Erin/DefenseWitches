from cmu_112_graphics import *
class Minion(App):
    def appStarted(self):
        self.cx=0
        self.cy=50
        self.minion1=self.loadImage('public/minion1.png')
        self.minion2=self.loadImage('public/minion2.png')
        self.direction="right"
        self.speed=3
        self.i=0
    def keyPressed(self,event):
        if event.key == "a":
            self.direction="left"
        elif event.key == "w":
            self.direction="front"
        elif event.key=="d":
            self.direction="right"
        elif event.key=='s':
            self.direction='back'
    def minionWalk(self,direction,canvas):
        if direction=="right":
            if self.i%self.speed==0:
                canvas.create_image(self.cx,self.cy, image=ImageTk.PhotoImage(self.minion1))
            else:
                canvas.create_image(self.cx,self.cy, image=ImageTk.PhotoImage(self.minion2))
    def redrawAll(self,canvas):
        Minion.minionWalk(self,self.direction,canvas)
    def timerFired(self):
        self.i+=1
        if self.direction=="right":
            self.cx+=self.speed
Minion(width=200, height=200)