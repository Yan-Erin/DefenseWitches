from cmu_112_graphics import *
import minions

class Daisy(App):
    def appStarted(self):
        self.cx=100
        self.cy=100
        self.DaisyFront1 = self.loadImage('public/DaisyFront1.png')
        self.DaisyFront2 =  self.loadImage('public/DaisyFront2.png')
        self.DaisySide1= self.loadImage('public/DaisySide1.png')
        self.DaisySide2= self.loadImage('public/DaisySide2.png')
        self.DaisySide3 = self.DaisySide1.transpose(Image.FLIP_LEFT_RIGHT)
        self.DaisySide4 = self.DaisySide2.transpose(Image.FLIP_LEFT_RIGHT)
        self.DaisyBack= self.loadImage('public/DaisyBack.png')
        self.attack=2
        self.speed=2
        self.range=1
        self.i=0
        self.direction="front"
    def daisyAttack(self, canvas, direction):
        if direction=="front":
            if self.i%self.speed==0:
                canvas.create_image(self.cx,self.cy, image=ImageTk.PhotoImage(self.DaisyFront1))
            else:
                canvas.create_image(self.cx,self.cy, image=ImageTk.PhotoImage(self.DaisyFront2))
        elif direction=="left":
            if self.i%self.speed==0:
                canvas.create_image(self.cx,self.cy, image=ImageTk.PhotoImage(self.DaisySide1))
            else:
                canvas.create_image(self.cx,self.cy, image=ImageTk.PhotoImage(self.DaisySide2))
        elif direction=="right":
            if self.i%self.speed==0:
                canvas.create_image(self.cx,self.cy, image=ImageTk.PhotoImage(self.DaisySide3))
            else:
                canvas.create_image(self.cx,self.cy, image=ImageTk.PhotoImage(self.DaisySide4))
        elif direction =="back":
            canvas.create_image(self.cx,self.cy, image=ImageTk.PhotoImage(self.DaisyBack))
    def timerFired(self):
        self.i+=1
    def keyPressed(self,event):
        if event.key == "a":
            self.direction="left"
        elif event.key == "w":
            self.direction="front"
        elif event.key=="d":
            self.direction="right"
        elif event.key=='s':
            self.direction='back'
            
    def redrawAll(self,canvas):
        Daisy.daisyAttack(self,canvas,self.direction)

Daisy(width=200, height=200)
