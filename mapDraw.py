import random
from cmu_112_graphics import *
import winsound
import minions
import time
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
    app.minionRight1=app.loadImage('public/minion1.png')
    app.minionRight2=app.loadImage('public/minion2.png')
    app.minionList=[]

    app.crab1=app.loadImage('public/crab1.png')
    app.crab2=app.loadImage('public/crab2.png')
    app.crabMinionList=[]
    for i in range(2):
        app.minionList.append(minions.Minion(app.c-i))
    for j in range(2):  
        app.crabMinionList.append(minions.CrabMinion(app.c-j))
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
                canvas.create_image((col+1)*50,(row+1)*50, image=ImageTk.PhotoImage(app.grass))
            if app.L[row][col]!=0:
                canvas.create_image((col+1)*50,(row+1)*50, image=ImageTk.PhotoImage(app.walkPath))
            if row==app.s[0] and col == app.s[1]:
                canvas.create_image((col+1)*50,(row+1)*50-5, image=ImageTk.PhotoImage(app.target))

def minionWalk(Minion,app, canvas):
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
    crabMinion.i+=1
    if crabMinion.i%crabMinion.speed==0:
        #print("1")
        canvas.create_image(crabMinion.cx,crabMinion.cy, image=ImageTk.PhotoImage(app.crab1))
        (x,y)=crabMinion.calculateNextDir(app.L)
        crabMinion.cx+=(y*50)
        crabMinion.cy+=(x*50)
    else:
        canvas.create_image(crabMinion.cx,crabMinion.cy, image=ImageTk.PhotoImage(app.crab2))

def redrawAll(app,canvas):
    drawMap(app,canvas)
    for i in app.minionList:
        minionWalk(i,app, canvas)
    for j in app.crabMinionList:
        crabMinionWalk(j,app, canvas)
runApp(width=800, height=600)



