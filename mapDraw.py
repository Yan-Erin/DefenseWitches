import random
from cmu_112_graphics import *
#from 15112 website
def appStarted(app):
    app.grass= app.loadImage("public/grass.png")
    app.walkPath= app.loadImage("public/walkPath.png")
    app.L = calculateMap(6,10)

def make2dList(rows, cols):
    return [ ([0] * cols) for row in range(rows) ]
def valid(L,row,col):
    if 0>row or row>=len(L):
        return False
    elif 0>col or col>=len(L[0]):
        return False
    elif L[row][col] != 0:
        return False
    return True
def add1s(L,row,col,sol,i=0):
    if  i > len(L[0])*1.5:
        return False
    if valid(L,row,col):
        L[row][col]=1
        if (row,col)==sol:
            return True
        if add1s(L, row + 1, col, sol,i+1) == True:
            return True
        if add1s(L, row, col+1, sol,i+1) == True:
            return True
        if add1s(L, row-1, col, sol,i+1) == True:
            return True
        L[row][col]= 0
    return False

def calculateMap(row, col):
    L= make2dList(row,col)
    c=random.randint(0,row)
    s=random.randint(0,row)
    if add1s(L,c,0,(s,col-1)):
        print(L)
        return L
    else:
        return None

def redrawAll(app,canvas):
    for row in range(len(app.L)):
        for col in range(len(app.L[0])):
            if app.L[row][col]==0:
                canvas.create_image((col+1)*50,row*50, image=ImageTk.PhotoImage(app.grass))
            if app.L[row][col]==1:
                canvas.create_image((col+1)*50,row*50, image=ImageTk.PhotoImage(app.walkPath))
runApp(width=550, height=300)



