from cmu_112_graphics import *
class Daisy(App):
    def appStarted(self):
        self.cx=100
        self.cy=100
        self.DaisyFront1 = self.loadImage('public/DaisyFront1.png')
        self.DaisyFront2 =  self.loadImage('public/DaisyFront2.png')
        self.DaisySide1= self.loadImage('public/DaisySide1.png')
        self.DaisySide2= self.loadImage('public/DaisySide2.png')
        self.attack=2
        self.speed=5
        self.range=1
        self.i=0
    def daisyAttack(canvas, self, dir):
        i=0
        if dir=="front":
            if self.i%2==0:
                canvas.create_image(self.cx,self.cy, image=ImageTk.PhotoImage(self.DaisyFront1))
            else:
                canvas.create_image(self.cx,self.cy, image=ImageTk.PhotoImage(self.DaisyFront2))
        elif dir=="left":
            if self.i%2==0:
                canvas.create_image(self.cx,self.cy, image=ImageTk.PhotoImage(self.DaisySide1))
            else:
                canvas.create_image(self.cx,self.cy, image=ImageTk.PhotoImage(self.DaisySide2))
    def timerFired(self):
        self.i+=1
    def redrawAll(self,canvas):
        Daisy.daisyAttack(canvas,self,"front")

Daisy(width=200, height=200)