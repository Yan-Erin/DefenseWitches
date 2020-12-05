import random
from cmu_112_graphics import *
import winsound
import minions
import time
import character
#from 15112 website
def appStarted(app):
    #winsound documentation
    #winsound.PlaySound('public/BGM01.wav', winsound.SND_ALIAS | winsound.SND_ASYNC | winsound.SND_LOOP)
    app.grass= app.loadImage("public/grass.png")
    app.walkPath= app.loadImage("public/walkPath.png")
    app.target =app.loadImage("public/Target.png")
    b = calculateMap(10,15)
    while type(b)!= tuple:
        b= calculateMap(10,15)
    app.L=b[0]
    app.s= b[1]
    app.c=b[2]
    app.points=160
    app.counter=0

    app.bar= app.loadImage('public/bar.png')
    app.pauseButton= app.loadImage('public/pauseButton.png')
    app.paused=False

    app.minionRight1=app.loadImage('public/minion1.png')
    app.minionRight2=app.loadImage('public/minion2.png')
    app.minionList=[]

    app.crab1=app.loadImage('public/crab1.png')
    app.crab2=app.loadImage('public/crab2.png')
    app.crabMinionList=[]
    

    app.DaisyFront1 = app.loadImage('public/DaisyFront1.png')
    app.DaisyFront2 =  app.loadImage('public/DaisyFront2.png')
    app.DaisySide1= app.loadImage('public/DaisySide1.png')
    app.DaisySide2= app.loadImage('public/DaisySide2.png')
    app.DaisySide3 = app.DaisySide1.transpose(Image.FLIP_LEFT_RIGHT)
    app.DaisySide4 = app.DaisySide2.transpose(Image.FLIP_LEFT_RIGHT)
    app.DaisyBack= app.loadImage('public/DaisyBack.png')
    app.explode= app.loadImage('public/explosionDaisy.png')
    app.DaisyList=[]

    app.menuOpenButton = app.loadImage("public/menuOpenButton.png")
    app.menu=False
    app.towerChoice=None

    app.DaisyButton = app.loadImage("public/DaisymenuOpen.png")
    app.minionList.append(minions.Minion(app.c))
    app.crabMinionList.append(minions.CrabMinion(app.c))
def make2dList(rows, cols):
    return [ ([0] * cols) for row in range(rows) ]

def valid(L,row,col):
    i=0
    if 0>row or row>=len(L):
        return False
    elif 0>col or col>=len(L[0]):
        return False
    elif L[row][col]!=0:
        return False
    if L[row-1][col]!=0:
        i+=1
    if L[row][col-1]!=0:
        i+=1
    if len(L)>row+1 and L[row+1][col]!=0:
        i+=1
    if  len(L[0])>col+1 and L[row][col+1]!=0:
        i+=1
    if len(L)>row+1 and len(L[0])>col+1 and  L[row+1][col+1]!=0:
        i+=1
    if L[row-1][col-1]!=0:
        i+=1
    if i>2:
        return False
    return True
def mousePressed(app,event):
    app.towerChoice=None
    if event.x>675 and event.x<725 and  event.y>25 and event.y<75:
        app.paused=not app.paused
        print(app.paused)
    if event.x>725 and event.x<775 and event.y>25 and event.y<75:
        print("hi")
        app.menu=not app.menu
    if app.menu==True:
        print(event.x,event.y)
        if event.x>660 and event.x<740 and event.y>78 and event.y<173:
            app.towerChoice="Daisy"
            print("hi")
    if app.towerChoice=="Daisy":
        app.DaisyList.append(character.Daisy(event.x,event.y))
def mouseDragged(app,event):
    if app.menu==True and app.towerChoice=="Daisy":
        app.DaisyList[len(app.DaisyList) -1].placed=False
        app.DaisyList[len(app.DaisyList) -1].cx=event.x
        app.DaisyList[len(app.DaisyList) -1].cy=event.y
def mouseReleased(app, event):
    if  app.menu==True and len(app.DaisyList)>0 and app.DaisyList[len(app.DaisyList) -1].placed==False:
        app.DaisyList[len(app.DaisyList) -1].placed=True
        k=app.DaisyList[len(app.DaisyList) -1]
        r,c =getCell(k.cx,k.cy)[0]
        r1,c1 =getCell(k.cx,k.cy)[1]
        r2,c2 =getCell(k.cx,k.cy)[2]
        print(app.points<160)
        if  app.points<160:
            app.DaisyList[-1].isValid=False
            app.DaisyList.remove(k)
        elif (app.L[c][r]!=0 or app.L[c1][r1]!=0 or app.L[c2][r2]!=0) and (k.placed==True):
            app.DaisyList[-1].isValid=False
            app.DaisyList.remove(k)
        else:
            app.DaisyList[-1].isValid=True
            app.points-=k.price
def add1s(L,row,col,sol,num=0):
    if valid(L,row,col):
        num+=1
        L[row][col]=num
        if (row,col)==sol:
            return True
        moves= [(0,1),(1,0),(0,-1), (-1,0)]
        if row >= sol[0]:
            move = random.choices(moves, weights= (11,3,2,7), k=1)[0]
        else:
            move = random.choices(moves, weights= (11,7,2,3) ,k=1)[0]
        i=0
        while not (valid(L,row+move[0], col+move[1])):
            i+=1
            #print(move)
            if i > 500:
                return False
            if row >= sol[0]:
                move = random.choices(moves, weights= (10,3,2,7),k=1)[0]
            else:
                move = random.choices(moves, weights= (10,7,2,3),k=1)[0]
        if add1s(L, row+move[0], col+move[1], sol, num+1) == True:
            return True
        else:
            L[row][col]= 0
            num-=1
    return False
def calculateMap(row, col):
    L= make2dList(row,col)
    c=random.randint(0,row)
    s=random.randint(0,row)
    sc=random.randint(col-3,col-1)
    while abs(c-s)<3:
        s=random.randint(0,row)
    if add1s(L,c,0,(s,sc)):
        print(L)
        return L,(s,sc),c
    else:
        return None
def drawMap(app,canvas):
    for row in range(len(app.L)):
        for col in range(len(app.L[0])):
            if app.L[row][col]==0:
                #112 website
                canvas.create_image((col+1)*50,(row+2)*50, image=ImageTk.PhotoImage(app.grass))
            if app.L[row][col]!=0:
                canvas.create_image((col+1)*50,(row+2)*50, image=ImageTk.PhotoImage(app.walkPath))
            if row==app.s[0] and col == app.s[1]:
                canvas.create_image((col+1)*50,(row+2)*50-5, image=ImageTk.PhotoImage(app.target))

def minionWalk(Minion,app, canvas):
    if not app.paused:
        Minion.i+=1
    if Minion.i%Minion.speed==0:
        #print("1")
        canvas.create_image(Minion.cx,Minion.cy, image=ImageTk.PhotoImage(app.minionRight1))
        (x,y)=Minion.calculateNextDir(app.L)
        Minion.cx+=(y*50)
        Minion.cy+=(x*50)
    else:
        canvas.create_image(Minion.cx,Minion.cy, image=ImageTk.PhotoImage(app.minionRight2))
def crabMinionWalk(crabMinion, app, canvas):
    if not app.paused:
        crabMinion.i+=1
    if crabMinion.i%crabMinion.speed==0:
        #print("1")
        canvas.create_image(crabMinion.cx,crabMinion.cy, image=ImageTk.PhotoImage(app.crab1))
        (x,y)=crabMinion.calculateNextDir(app.L)
        crabMinion.cx+=(y*50)
        crabMinion.cy+=(x*50)
    else:
        canvas.create_image(crabMinion.cx,crabMinion.cy, image=ImageTk.PhotoImage(app.crab2))

def daisyAttack(Daisy, app, canvas, direction):
    if not app.paused:
        Daisy.i+=1
    if Daisy.placed==True and direction=="front":
        if Daisy.i%Daisy.speed==0:
            shot=Daisy.shoot(app.minionList,app.crabMinionList)
            if shot!=None:
                canvas.create_image(shot[0], shot[1], image=ImageTk.PhotoImage(app.explode))
                canvas.create_image(Daisy.cx,Daisy.cy, image=ImageTk.PhotoImage(app.DaisyFront2))
            else:
                canvas.create_image(Daisy.cx,Daisy.cy, image=ImageTk.PhotoImage(app.DaisyFront1))
        else:
            canvas.create_image(Daisy.cx,Daisy.cy, image=ImageTk.PhotoImage(app.DaisyFront1))
    elif Daisy.placed==True and direction=="left":
        shot=Daisy.shoot(app.minionList,app.crabMinionList)
        if Daisy.i%Daisy.speed==0:
            if shot!=None:
                canvas.create_image(shot[0], shot[1], image=ImageTk.PhotoImage(app.explode))
                canvas.create_image(Daisy.cx,Daisy.cy, image=ImageTk.PhotoImage(app.DaisySide2))
            else:
                canvas.create_image(Daisy.cx,Daisy.cy, image=ImageTk.PhotoImage(app.DaisySide1))
        else:
            canvas.create_image(Daisy.cx,Daisy.cy, image=ImageTk.PhotoImage(app.DaisySide1))
    elif Daisy.placed==True and direction=="right":
        shot=Daisy.shoot(app.minionList,app.crabMinionList)
        if Daisy.i%Daisy.speed==0:
            if shot!=None:
                canvas.create_image(shot[0], shot[1], image=ImageTk.PhotoImage(app.explode))
                canvas.create_image(Daisy.cx,Daisy.cy, image=ImageTk.PhotoImage(app.DaisySide4))
            else:
                canvas.create_image(Daisy.cx,Daisy.cy, image=ImageTk.PhotoImage(app.DaisySide3))
        else:
            canvas.create_image(Daisy.cx,Daisy.cy, image=ImageTk.PhotoImage(app.DaisySide3))
    elif Daisy.placed==True and direction =="back":
        shot=Daisy.shoot(app.minionList,app.crabMinionList)
        if shot!=None:
            canvas.create_image(shot[0], shot[1], image=ImageTk.PhotoImage(app.explode))
        canvas.create_image(Daisy.cx, Daisy.cy, image=ImageTk.PhotoImage(app.DaisyBack))
    else: 
        canvas.create_oval(Daisy.cx-Daisy.range*50,Daisy.cy-Daisy.range*50, Daisy.cx+Daisy.range*50, Daisy.cy+Daisy.range*50)
        canvas.create_image(Daisy.cx,Daisy.cy, image=ImageTk.PhotoImage(app.DaisyFront1))
def getCell(x,y):
    #top left
    x0=x-50//2
    y0=y-70//2

    #bottom right
    x3=x+50//2
    y3=y+70//2
    return [(x//50-1, y//50-2), (x0//50-1, y0//50-1),(x3//50-1, y3//50-2)]
def timerFired(app):
    if not app.paused:
        app.counter+=1
        if app.counter%50==0:
            app.crabMinionList.append(minions.CrabMinion(app.c))
            app.minionList.append(minions.Minion(app.c))
        for i in app.minionList:
            if i.health<=0:
                app.points+=i.money
                app.minionList.remove(i)
        for j in app.crabMinionList:
            if j.health<=0:
                app.points+=j.money
                app.crabMinionList.remove(j)
def redrawAll(app,canvas):
    drawMap(app,canvas)
    canvas.create_image(348, 50, image=ImageTk.PhotoImage(app.bar))
    canvas.create_text(480, 50, text=app.points, font='Arial 18', fill="#302519")
    canvas.create_image(700, 50, image=ImageTk.PhotoImage(app.pauseButton))
    for i in app.minionList:
        if i.drawHealthBar==True:
            canvas.create_rectangle(i.cx-15,i.cy-50,i.cx+15,i.cy-45, fill='grey' )
            canvas.create_rectangle(i.cx-15,i.cy-50,i.cx+15*(i.health/i.totalHealth),i.cy-45, fill='red' )
        minionWalk(i,app, canvas)
    for j in app.crabMinionList:
        if j.drawHealthBar==True:
            canvas.create_rectangle(j.cx-15,j.cy-50,j.cx+15,j.cy-45, fill='grey' )
            canvas.create_rectangle(j.cx-15,j.cy-50,j.cx+15*(j.health/j.totalHealth),j.cy-45, fill='red' )
        crabMinionWalk(j,app, canvas)
    for k in app.DaisyList:
        daisyAttack(k, app, canvas, k.direction)
    canvas.create_image(750, 50, image=ImageTk.PhotoImage(app.menuOpenButton))
    if app.menu==True:
        canvas.create_image(700, 125, image=ImageTk.PhotoImage(app.DaisyButton))
runApp(width=800, height=600)



