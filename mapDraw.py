import random
from cmu_112_graphics import *
import winsound
import minions
import time
import character


def getCell(x,y):
        #top left
        x0=x-50//2
        y0=y-70//2

        #bottom right
        x3=x+50//2
        y3=y+70//2
        return [(x//50-1, y//50-2), (x0//50-1, y0//50-1),(x3//50-1, y3//50-2)]
def add1s(L,row,col,sol,num=0):#inspired by knights tour
        if valid(L,row,col):
            if isinstance(num, int):
                num+=1
            L[row][col]=num
            if (row,col)==sol:
                return True
            moves= [(0,1),(1,0),(0,-1), (-1,0)]
            if row >= sol[0]:
                move = random.choices(moves, weights= (10,3,2,7), k=1)[0]
            else:
                move = random.choices(moves, weights= (10,7,2,3) ,k=1)[0]
            i=0
            while not (valid(L,row+move[0], col+move[1])):
                i+=1
                #print(move)
                if i > 500:
                    return False
                if row >= sol[0]:
                    move = random.choices(moves, weights= (11,3,2,7),k=1)[0]
                else:
                    move = random.choices(moves, weights= (11,7,2,3),k=1)[0]
            if isinstance(num, int):
                if add1s(L, row+move[0], col+move[1], sol, num+1) == True:
                    return True
                else:
                    L[row][col]= 0
                    num-=1
            else:
                if add1s(L, row+move[0], col+move[1], sol, num+1) == True:
                    return True
                else:
                    L[row][col]= 0
        return False
def harderAdd1(L,row,col,sol, visted):
    if (row,col)==sol:
        L[row][col]=1
        print(sol)
        return True
    moves= [(0,1),(1,0),(0,-1), (-1,0)]
    for move in moves:
        move=random.choices(moves, weights= (10,3,2,7), k=1)[0]
        if (valid(L,row+move[0], col+move[1])):
            L[row+move[0]][col+move[1]]=1
            visted.add((row+move[0],col+move[1]))
            harderAdd1(L, row+move[0], col+move[1], sol,visted)
def solveMap(L,r,c,s,sc): #inspired by 15112
    visited = []
    targetRow,targetCol =s,sc
    def solve(row,col):
        if (row,col) in visited: 
            return False
        visited.append((row,col))
        if (row,col)==(targetRow,targetCol): return True
        for drow,dcol in [(0,1),(1,0),(-1,0),(0,-1)]:
            if  isValid(L, row+drow,col+dcol):
                print("hi")
                if solve(row+drow,col+dcol): return True
        visited.remove((row,col))
        return False
    return visited if solve(r,c) else None
def isValid(L,row,col):
    if 0>row or row>=len(L):
        return False
    elif 0>col or col>=len(L[0]):
        return False
    elif L[row][col]==0:
        return False
    else:
        return True
def calculateMap(row, col,diff):
    L= make2dList(row,col)
    c=random.randint(0,row)
    s=random.randint(0,row)
    sc=random.randint(col-3,col-1)
    while abs(c-s)<3:
        s=random.randint(0,row)
    if diff<5 and add1s(L,c,0,(s,sc)):
        if diff<=3:
            if L[s][sc]>22*diff and L[s][sc]<35*diff:
                return L,(s,sc),c
        elif diff==4:
            if L[s][sc]>22*diff:
                return L,(s,sc),c
        else:
            return None
    elif diff==5:
        visted=set((c,0))
        harderAdd1(L,c,0,(s,sc), visted)
        L[c][0]=1

        v=solveMap(L,c,0,s,sc)
        while v==None:
            L= make2dList(row,col)
            visted=set((c,0))
            harderAdd1(L,c,0,(s,sc), visted)
            L[c][0]=1
            v=solveMap(L,c,0,s,sc)
        for i in range(len(L)):
            for j in range(len(L[0])):
                if (i,j) in v:
                    L[i][j]=v.index((i,j))+1
                else:
                    L[i][j]=0

        return(L,(s,sc),c)
    else:
        return None 
def addPondandTrees(L):
    for i in range(len(L)):
        for j in range(len(L[0])):
            choice = random.choices([0,1], weights=(10,1),k=1)
            if L[i][j] ==0 and choice[0]==1:
                L[i][j] = "*"
    for i in range(len(L)-3):
        for j in range(len(L[0])-3):
            if (L[i][j] ==0 and L[i+1][j]==0 and L[i][j+1]==0 and L[i+1][j+1]==0 and L[i+2][j]==0 and L[i+1][j+2]==0 and L[i+2][j+2]==0
            and L[i+2][j+1]==0 and L[i][j+2]==0):
                choice1 = random.choices([0,1], weights=(10,12),k=1)
                if choice1[0] ==1:
                    L[i][j] ="w"
                    L[i+1][j]="w"
                    L[i][j+1]="w"
                    L[i+1][j+1]="w"
                    L[i+2][j]="w" 
                    L[i+1][j+2]="w" 
                    L[i+2][j+2]="w"
                    L[i+2][j+1]="w"
                    L[i][j+2]="w"
#taken from 15112 website 
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


class SplashScreenMode(Mode):
    def appStarted(mode):
        mode.start= mode.loadImage("public/StartPage.png") #from https://www.aweapps.com/defense-witches-quick-review-2koma-manga-tower-defense
    def redrawAll(mode, canvas):
        canvas.create_image(400, 300, image=ImageTk.PhotoImage(mode.start))

    def mousePressed(mode, event):
        print(event.y)
        if event.x>58 and event.x<262 and event.y>265 and event.y<313:
            mode.app.setActiveMode(mode.app.gameMode)
        elif event.x>58 and event.x<262 and event.y>457 and event.y<500:
            mode.app.setActiveMode(mode.app.helpMode)
        elif event.x>58 and event.x<262 and event.y>330 and event.y<375:
            mode.app.setActiveMode(mode.app.optionsScreen)
        elif event.x>58 and event.x<262 and event.y>400 and event.y<441:
            mode.app.setActiveMode(mode.app.creditsPage)

class GameMode(Mode):
    def appStarted(mode):
        print(mode.app.unlimitedMoney)
        #winsound documentation
        if mode.app.bgMusic==True:
            winsound.PlaySound('public/BGM01.wav', winsound.SND_ALIAS | winsound.SND_ASYNC | winsound.SND_LOOP) #music from https://www.youtube.com/watch?v=3PytsOJqyoc
        if mode.app.color==False:
            mode.grass= mode.loadImage("public/grass.png") # from https://baudattitude.com/2012/07/10/witch-touching/
            mode.walkPath= mode.loadImage("public/walkPath.png") #from https://www.aweapps.com/defense-witches-quick-review-2koma-manga-tower-defense
            mode.tree= mode.loadImage("public/Tree.png") #From https://favpng.com/png_view/trees-drawing-watercolor-painting-tree-pencil-sketch-png/URn9j9Cz
        else:
            mode.grass= mode.loadImage("public/border.png") # from https://www.youtube.com/watch?v=CmCCAxJpzI8&ab_channel=DwNicola
            mode.walkPath= mode.loadImage("public/Path3.png") #from https://www.youtube.com/watch?v=CmCCAxJpzI8&ab_channel=DwNicola
            mode.tree= mode.loadImage("public/obstacle.png") #From https://www.youtube.com/watch?v=CmCCAxJpzI8&ab_channel=DwNicola
        mode.target =mode.loadImage("public/Target.png") #From https://www.aweapps.com/defense-witches-quick-review-2koma-manga-tower-defense
        mode.water= mode.loadImage("public/water.jpg") # from https://apkpure.com/defense-witches/jp.newgate.game.android.dw
        b = calculateMap(10,15,mode.app.difficulty)
        while type(b)!= tuple:
            b= calculateMap(10,15,mode.app.difficulty)
        try:
            deadEnds(b[0])
        except:
            pass
        addPondandTrees(b[0])
        print(b[0])
        mode.L=b[0]
        mode.s= b[1]
        mode.c=b[2]
        mode.score=0
        mode.points=300
        mode.counter=0
        mode.lives=20

        mode.bar= mode.loadImage('public/bar.png') # from https://baudattitude.com/2012/07/10/witch-touching/
        mode.pauseButton= mode.loadImage('public/pauseButton.png') #From https://apkpure.com/defense-witches/jp.newgate.game.android.dw
        mode.paused=False
        mode.GameOverText=mode.loadImage('public/GameOverText.png') #photoshoped by me
        mode.gameOver=False

        mode.waveNumber=0
        mode.minionWave=20
        mode.wave=[(3,5), (8,4),(4,7),(9,10),(4,16)]
        mode.minionRight1=mode.loadImage('public/minion1.png') # from https://baudattitude.com/2012/07/10/witch-touching/
        mode.minionRight2=mode.loadImage('public/minion2.png') # from https://baudattitude.com/2012/07/10/witch-touching/
        mode.minionList=[]

        mode.crab1=mode.loadImage('public/crab1.png')#From https://www.aweapps.com/defense-witches-quick-review-2koma-manga-tower-defense
        mode.crab2=mode.loadImage('public/crab2.png')#From https://www.aweapps.com/defense-witches-quick-review-2koma-manga-tower-defense
        mode.crabMinionList=[]
        

        mode.DaisyFront1 = mode.loadImage('public/DaisyFront1.png')#From https://www.aweapps.com/defense-witches-quick-review-2koma-manga-tower-defense
        mode.DaisyFront2 =  mode.loadImage('public/DaisyFront2.png')#From https://www.aweapps.com/defense-witches-quick-review-2koma-manga-tower-defense
        mode.DaisySide1= mode.loadImage('public/DaisySide1.png')#From https://www.aweapps.com/defense-witches-quick-review-2koma-manga-tower-defense
        mode.DaisySide2= mode.loadImage('public/DaisySide2.png')#From https://www.aweapps.com/defense-witches-quick-review-2koma-manga-tower-defense
        mode.DaisySide3 = mode.DaisySide1.transpose(Image.FLIP_LEFT_RIGHT)
        mode.DaisySide4 = mode.DaisySide2.transpose(Image.FLIP_LEFT_RIGHT)
        mode.DaisyBack1= mode.loadImage('public/DaisyBack2.png')#From https://www.aweapps.com/defense-witches-quick-review-2koma-manga-tower-defense
        mode.DaisyBack2= mode.loadImage('public/DaisyBack1.png')#From https://www.aweapps.com/defense-witches-quick-review-2koma-manga-tower-defense
        mode.DaisyBack3 = mode.DaisyBack1.transpose(Image.FLIP_LEFT_RIGHT)
        mode.DaisyBack4 = mode.DaisyBack2.transpose(Image.FLIP_LEFT_RIGHT)
        mode.DaisyBack1= mode.loadImage('public/DaisyBack2.png')#From https://www.aweapps.com/defense-witches-quick-review-2koma-manga-tower-defense
        mode.DaisyBack2= mode.loadImage('public/DaisyBack1.png')#From https://www.aweapps.com/defense-witches-quick-review-2koma-manga-tower-defense
        mode.explode= mode.loadImage('public/explosionDaisy.png')#From https://www.aweapps.com/defense-witches-quick-review-2koma-manga-tower-defense
        mode.DaisyUpgrade= mode.loadImage('public/DaisyUpgrade.png')#From https://www.aweapps.com/defense-witches-quick-review-2koma-manga-tower-defense
        mode.FirstButton=mode.loadImage('public/FirstButton.png')#i made this one myself
        mode.LastButton=mode.loadImage('public/LastButton.png')#i made this one myself
        mode.DaisyList=[]
        mode.d=0

        mode.blueExplosion= mode.loadImage('public/chloeAttack.png')# from https://baudattitude.com/2012/07/10/witch-touching/
        mode.ChloeFront1 = mode.loadImage('public/Chloe1.png')# from https://baudattitude.com/2012/07/10/witch-touching/
        mode.ChloeFront2 =  mode.loadImage('public/Chloe2.png')# from https://baudattitude.com/2012/07/10/witch-touching/
        mode.ChloeFront3 = mode.loadImage('public/Chloe3.png')# from https://baudattitude.com/2012/07/10/witch-touching/
        mode.ChloeButton=  mode.loadImage("public/chloeMenuButton.png")  # from https://baudattitude.com/2012/07/10/witch-touching/
        mode.ChloeUpgrade= mode.loadImage('public/ChloeUpgrade.png') # from https://www.youtube.com/watch?v=szHTFvsXR-8&ab_channel=AndroidGamerTMG
        mode.ChloeList=[]
    
        mode.menuOpenButton = mode.loadImage("public/menuOpenButton.png")# from https://baudattitude.com/2012/07/10/witch-touching/

        mode.menu=False
        mode.towerChoice=None

        mode.DaisyButton = mode.loadImage("public/DaisymenuOpen.png")#From https://www.youtube.com/watch?v=szHTFvsXR-8&ab_channel=AndroidGamerTMG
        mode.minionList.append(minions.Minion(mode.c))
        mode.crabMinionList.append(minions.CrabMinion(mode.c))
    def keyPressed(mode,event):
        if event.keycode==32:
            GameMode.appStarted(mode)
        if event.keycode==8:
            mode.app.setActiveMode(mode.app.splashScreenMode)
    def mousePressed(mode,event):
        mode.towerChoice=None
        if event.x>675 and event.x<725 and  event.y>25 and event.y<75:
            mode.paused=not mode.paused
            print(mode.paused)
        if event.x>725 and event.x<775 and event.y>25 and event.y<75:
            mode.menu=not mode.menu
        if mode.menu==True:
            print(event.x,event.y)
            if event.x>660 and event.x<740 and event.y>78 and event.y<173:
                mode.towerChoice="Daisy"
            elif event.x>580 and event.x<660 and event.y>78 and event.y<173:
                mode.towerChoice="Chloe"
        for i in mode.DaisyList:
            if event.x> i.cx-25 and event.x<i.cx+25 and event.y>i.cy-35 and event.y<i.cy+35 and mode.d<1:
                i.clicked=not i.clicked
                if i.clicked==True:
                    mode.d+=1
                else:
                    mode.d-=1
            elif i.clicked==True:
                if event.x>750 and event.x<800 and event.y<450 and event.y>350:
                    i.clicked=False
                    mode.d-=1
                if event.x>77 and event.x<235 and event.y>511 and event.y<567 :
                    if mode.app.unlimitedMoney==False and mode.points>160:
                        i.upgrade()
                        mode.points-=160
                    elif mode.app.unlimitedMoney:
                        i.upgrade()
                if event.x>318 and event.x<490 and event.y>511 and event.y<567:
                    mode.DaisyList.remove(i)
                    mode.points+=128
                    mode.d-=1
                if event.x>320 and event.x<420 and event.y>450 and event.y<490:
                    i.attackmethod=not i.attackmethod

        for c in mode.ChloeList:
            if event.x> c.cx-25 and event.x<c.cx+25 and event.y>c.cy-35 and event.y<c.cy+35 and mode.d<1:
                c.clicked=not c.clicked
                if c.clicked==True:
                    mode.d+=1
                else:
                    mode.d-=1
            elif c.clicked==True:
                if event.x>750 and event.x<800 and event.y<450 and event.y>350:
                    c.clicked=False
                    mode.d-=1
                if event.x>77 and event.x<235 and event.y>511 and event.y<567:
                    if mode.app.unlimitedMoney==False and mode.points>160:
                        c.upgrade()
                        mode.points-=160
                    elif mode.app.unlimitedMoney:
                        c.upgrade()
                if event.x>318 and event.x<490 and event.y>511 and event.y<567:
                    mode.ChloeList.remove(c)
                    mode.points+=128
                    mode.d-=1


        if mode.towerChoice=="Daisy":
            mode.DaisyList.append(character.Daisy(event.x,event.y))
        elif mode.towerChoice=="Chloe":
            mode.ChloeList.append(character.Chloe(event.x,event.y))
    def mouseDragged(mode,event):
        if mode.menu==True and mode.towerChoice=="Daisy":
            mode.DaisyList[len(mode.DaisyList) -1].placed=False
            mode.DaisyList[len(mode.DaisyList) -1].cx=event.x
            mode.DaisyList[len(mode.DaisyList) -1].cy=event.y
        elif mode.menu==True and mode.towerChoice=="Chloe":
            mode.ChloeList[len(mode.ChloeList) -1].placed=False
            mode.ChloeList[len(mode.ChloeList) -1].cx=event.x
            mode.ChloeList[len(mode.ChloeList) -1].cy=event.y
    def mouseReleased(mode, event):
        if  mode.menu==True and mode.towerChoice=="Daisy" and len(mode.DaisyList)>0 and mode.DaisyList[len(mode.DaisyList) -1].placed==False:
            mode.DaisyList[len(mode.DaisyList) -1].placed=True
            k=mode.DaisyList[len(mode.DaisyList) -1]
            r,c =getCell(k.cx,k.cy)[0]
            r1,c1 =getCell(k.cx,k.cy)[1]
            r2,c2 =getCell(k.cx,k.cy)[2]
            if  mode.points<160 and (mode.app.unlimitedMoney==False):
                mode.DaisyList[-1].isValid=False
                mode.DaisyList.remove(k)
            elif (mode.L[c][r]!=0 or mode.L[c1][r1]!=0 or mode.L[c2][r2]!=0) and (k.placed==True):
                mode.DaisyList[-1].isValid=False
                mode.DaisyList.remove(k)
            else:
                mode.DaisyList[-1].isValid=True
                mode.L[c][r]="d"
                mode.L[c1][r1]="d"
                mode.L[c2][r2]="d"
                if mode.app.unlimitedMoney==False:
                    mode.points-=k.price
        elif  mode.menu==True and mode.towerChoice=="Chloe" and len(mode.ChloeList)>0 and mode.ChloeList[len(mode.ChloeList) -1].placed==False:
            mode.ChloeList[len(mode.ChloeList) -1].placed=True
            k=mode.ChloeList[len(mode.ChloeList) -1]
            r,c =getCell(k.cx,k.cy)[0]
            r1,c1 =getCell(k.cx,k.cy)[1]
            r2,c2 =getCell(k.cx,k.cy)[2]
            if  mode.points<k.price and mode.app.unlimitedMoney==False:
                mode.ChloeList[-1].isValid=False
                mode.ChloeList.remove(k)
            elif (mode.L[c][r]!=0 or mode.L[c1][r1]!=0 or mode.L[c2][r2]!=0) and (k.placed==True):
                mode.ChloeList[-1].isValid=False
                mode.ChloeList.remove(k)
            else:
                mode.ChloeList[-1].isValid=True
                mode.L[c][r]="d"
                mode.L[c1][r1]="d"
                mode.L[c2][r2]="d"
                if mode.app.unlimitedMoney==False:
                    mode.points-=k.price
    def drawMap(mode,canvas):
        for row in range(len(mode.L)):
            for col in range(len(mode.L[0])):
                if mode.L[row][col]==0 or mode.L[row][col]=="*" or  mode.L[row][col]=="d" :
                    #112 website
                    canvas.create_image((col+1)*50,(row+2)*50, image=ImageTk.PhotoImage(mode.grass))
                if mode.L[row][col]=="w":
                    canvas.create_image((col+1)*50,(row+2)*50, image=ImageTk.PhotoImage(mode.water))
                elif mode.L[row][col]=="*":
                    canvas.create_image((col+1)*50,(row+2)*50, image=ImageTk.PhotoImage(mode.tree))
                elif isinstance(mode.L[row][col],int) and mode.L[row][col]>0 or mode.L[row][col]=="end":
                    canvas.create_image((col+1)*50,(row+2)*50, image=ImageTk.PhotoImage(mode.walkPath))
                if row==mode.s[0] and col == mode.s[1]:
                    canvas.create_image((col+1)*50,(row+2)*50-5, image=ImageTk.PhotoImage(mode.target))

    def minionWalk(Minion,mode, canvas):
        if not mode.paused and (not mode.gameOver):
            Minion.i+=1
        if Minion.i%Minion.speed==0:
            canvas.create_image(Minion.cx,Minion.cy, image=ImageTk.PhotoImage(mode.minionRight1))
            if not mode.paused and not mode.gameOver:
                if mode.app.minionShortestPath==True:
                    (x,y)=Minion.calcShortestPath2(mode.L)
                else:
                    (x,y)=Minion.calculateNextDir(mode.L)
                Minion.cx+=(y*50)
                Minion.cy+=(x*50)
        else:
            canvas.create_image(Minion.cx,Minion.cy, image=ImageTk.PhotoImage(mode.minionRight2))
    def crabMinionWalk(crabMinion, mode, canvas):
        if not mode.paused and (not mode.gameOver):
            crabMinion.i+=1
        if crabMinion.i%crabMinion.speed==0:
            canvas.create_image(crabMinion.cx,crabMinion.cy, image=ImageTk.PhotoImage(mode.crab1))
            if not mode.paused and (not mode.gameOver):
                if mode.app.minionShortestPath==True:
                    (x,y)=crabMinion.calcShortestPath2(mode.L)
                else:
                    (x,y)=crabMinion.calculateNextDir(mode.L)
                crabMinion.cx+=(y*50)
                crabMinion.cy+=(x*50)
        else:
            canvas.create_image(crabMinion.cx,crabMinion.cy, image=ImageTk.PhotoImage(mode.crab2))
    def chloeAttack(Chloe, mode, canvas):
        if not mode.paused and (not mode.gameOver):
            Chloe.i+=1
        if Chloe.placed==True and not mode.paused and (not mode.gameOver) and Chloe.i%Chloe.speed==0:
            if Chloe.i%Chloe.speed==0 and not mode.paused and (not mode.gameOver):
                shot= Chloe.shoot(mode.minionList,mode.crabMinionList)
                if shot==True and not mode.paused and (not mode.gameOver):
                    ex = mode.scaleImage(mode.blueExplosion,(4/10)*Chloe.range)
                    canvas.create_image(Chloe.cx,Chloe.cy, image=ImageTk.PhotoImage(ex))
                    canvas.create_image(Chloe.cx,Chloe.cy, image=ImageTk.PhotoImage(mode.ChloeFront1))
                elif shot==True and Chloe.i%Chloe.speed==1 and not mode.paused and (not mode.gameOver):
                    canvas.create_image(Chloe.cx,Chloe.cy, image=ImageTk.PhotoImage(mode.ChloeFront3))
                else:
                    canvas.create_image(Chloe.cx,Chloe.cy, image=ImageTk.PhotoImage(mode.ChloeFront2))
            else:
                canvas.create_image(Chloe.cx,Chloe.cy, image=ImageTk.PhotoImage(mode.ChloeFront3))
        else:
            canvas.create_image(Chloe.cx,Chloe.cy, image=ImageTk.PhotoImage(mode.ChloeFront2))
    def daisyAttack(Daisy, mode, canvas, direction):
        if not mode.paused and (not mode.gameOver):
            Daisy.i+=1
        if Daisy.placed==True and direction=="front" and not mode.paused and (not mode.gameOver):
            if Daisy.i%Daisy.speed==0 and not mode.paused and (not mode.gameOver):
                shot=Daisy.shoot(mode.minionList,mode.crabMinionList)
                if shot!=None and not mode.paused and (not mode.gameOver):
                    canvas.create_image(shot[0], shot[1], image=ImageTk.PhotoImage(mode.explode))
                    canvas.create_image(Daisy.cx,Daisy.cy, image=ImageTk.PhotoImage(mode.DaisyFront2))
                else:
                    canvas.create_image(Daisy.cx,Daisy.cy, image=ImageTk.PhotoImage(mode.DaisyFront1))
            else:
                canvas.create_image(Daisy.cx,Daisy.cy, image=ImageTk.PhotoImage(mode.DaisyFront1))
        elif Daisy.placed==True and direction=="left"and not mode.paused and (not mode.gameOver):
            shot=Daisy.shoot(mode.minionList,mode.crabMinionList)
            if Daisy.i%Daisy.speed==0 and not mode.paused and (not mode.gameOver):
                if shot!=None and not mode.paused and (not mode.gameOver):
                    canvas.create_image(shot[0], shot[1], image=ImageTk.PhotoImage(mode.explode))
                    canvas.create_image(Daisy.cx,Daisy.cy, image=ImageTk.PhotoImage(mode.DaisySide2))
                else:
                    canvas.create_image(Daisy.cx,Daisy.cy, image=ImageTk.PhotoImage(mode.DaisySide1))
            else:
                canvas.create_image(Daisy.cx,Daisy.cy, image=ImageTk.PhotoImage(mode.DaisySide1))
        elif Daisy.placed==True and direction=="right"and not mode.paused and (not mode.gameOver):
            shot=Daisy.shoot(mode.minionList,mode.crabMinionList)
            if Daisy.i%Daisy.speed==0 and not mode.paused and (not mode.gameOver):
                if shot!=None and not mode.paused and (not mode.gameOver):
                    canvas.create_image(shot[0], shot[1], image=ImageTk.PhotoImage(mode.explode))
                    canvas.create_image(Daisy.cx,Daisy.cy, image=ImageTk.PhotoImage(mode.DaisySide4))
                else:
                    canvas.create_image(Daisy.cx,Daisy.cy, image=ImageTk.PhotoImage(mode.DaisySide3))
            else:
                canvas.create_image(Daisy.cx,Daisy.cy, image=ImageTk.PhotoImage(mode.DaisySide3))
        elif Daisy.placed==True and direction=="back right"and not mode.paused and (not mode.gameOver):
            shot=Daisy.shoot(mode.minionList,mode.crabMinionList)
            if Daisy.i%Daisy.speed==0 and not mode.paused and (not mode.gameOver):
                if shot!=None and not mode.paused and (not mode.gameOver):
                    canvas.create_image(shot[0], shot[1], image=ImageTk.PhotoImage(mode.explode))
                    canvas.create_image(Daisy.cx,Daisy.cy, image=ImageTk.PhotoImage(mode.DaisyBack4))
                else:
                    canvas.create_image(Daisy.cx,Daisy.cy, image=ImageTk.PhotoImage(mode.DaisyBack3))
            else:
                canvas.create_image(Daisy.cx,Daisy.cy, image=ImageTk.PhotoImage(mode.DaisyBack3))
        elif Daisy.placed==True and direction=="back left"and not mode.paused and (not mode.gameOver):
            shot=Daisy.shoot(mode.minionList,mode.crabMinionList)
            if Daisy.i%Daisy.speed==0 and not mode.paused and (not mode.gameOver):
                if shot!=None and not mode.paused and (not mode.gameOver):
                    canvas.create_image(shot[0], shot[1], image=ImageTk.PhotoImage(mode.explode))
                    canvas.create_image(Daisy.cx,Daisy.cy, image=ImageTk.PhotoImage(mode.DaisyBack2))
                else:
                    canvas.create_image(Daisy.cx,Daisy.cy, image=ImageTk.PhotoImage(mode.DaisyBack1))
            else:
                canvas.create_image(Daisy.cx,Daisy.cy, image=ImageTk.PhotoImage(mode.DaisyBack1))
        else: 
            canvas.create_oval(Daisy.cx-Daisy.range*50,Daisy.cy-Daisy.range*50, Daisy.cx+Daisy.range*50, Daisy.cy+Daisy.range*50)
            canvas.create_image(Daisy.cx,Daisy.cy, image=ImageTk.PhotoImage(mode.DaisyFront1))
    def timerFired(mode):
        if mode.lives<=0:
            mode.gameOver=True
        if not mode.paused and (not mode.gameOver):
            mode.counter+=1
            if mode.counter%200==1:
                mode.minionWave-=1
            if mode.counter%mode.minionWave==10:
                mode.crabMinionList.append(minions.CrabMinion(mode.c))
            if mode.counter%mode.minionWave==10:
                mode.minionList.append(minions.Minion(mode.c))
            for i in mode.minionList:
                if i.health<=0:
                    mode.points+=i.money
                    mode.score+=i.score
                    mode.minionList.remove(i)
                if minions.getCell(i.cx,i.cy)[1]==mode.s[0] and minions.getCell(i.cx,i.cy)[0]==mode.s[1]:
                    mode.minionList.remove(i)
                    mode.lives-=1
            for j in mode.crabMinionList:
                if j.health<=0:
                    mode.points+=j.money
                    mode.score+=j.score
                    mode.crabMinionList.remove(j)
                if minions.getCell(j.cx,j.cy)[1]==mode.s[0] and minions.getCell(j.cx,j.cy)[0]==mode.s[1]:
                    mode.crabMinionList.remove(j)
                    mode.lives-=1

    def redrawAll(mode,canvas):
        GameMode.drawMap(mode,canvas)
        canvas.create_image(348, 50, image=ImageTk.PhotoImage(mode.bar))
        canvas.create_text(150, 50, text=f"{mode.waveNumber}/20", font='Arial 18', fill="#302519")
        canvas.create_text(310, 50, text=mode.score, font='Arial 18', fill="#302519")
        canvas.create_text(480, 50, text=mode.points, font='Arial 18', fill="#302519")
        canvas.create_text(600, 50, text=f"{mode.lives}/20", font='Arial 18', fill="#302519")
        canvas.create_image(700, 50, image=ImageTk.PhotoImage(mode.pauseButton))
        for i in mode.minionList:
            if i.drawHealthBar==True:
                canvas.create_rectangle(i.cx-15,i.cy-50,i.cx+15,i.cy-45, fill='grey' )
                canvas.create_rectangle(i.cx-15,i.cy-50,i.cx+15*(i.health/i.totalHealth),i.cy-45, fill='red' )
            GameMode.minionWalk(i,mode, canvas)
        for j in mode.crabMinionList:
            if j.drawHealthBar==True:
                canvas.create_rectangle(j.cx-15,j.cy-50,j.cx+15,j.cy-45, fill='grey' )
                canvas.create_rectangle(j.cx-15,j.cy-50,j.cx+15*(j.health/j.totalHealth),j.cy-45, fill='red' )
            GameMode.crabMinionWalk(j,mode, canvas)
        for k in mode.DaisyList:
            GameMode.daisyAttack(k, mode, canvas, k.direction)
            if k.clicked==True:
                canvas.create_oval(k.cx-k.range*50,k.cy-k.range*50, k.cx+k.range*50, k.cy+ k.range*50)
                canvas.create_image(400,475, image=ImageTk.PhotoImage(mode.DaisyUpgrade))
                if k.attackmethod ==True:
                    canvas.create_image(370,470, image=ImageTk.PhotoImage(mode.FirstButton))
                else:
                    canvas.create_image(370,470, image=ImageTk.PhotoImage(mode.LastButton))
        for c in mode.ChloeList:
            GameMode.chloeAttack(c, mode, canvas)
            if c.clicked==True:
                canvas.create_oval(c.cx-c.range*50,c.cy-c.range*50, c.cx+c.range*50, c.cy+ c.range*50)
                canvas.create_image(400,475, image=ImageTk.PhotoImage(mode.ChloeUpgrade))
        
        canvas.create_image(750, 50, image=ImageTk.PhotoImage(mode.menuOpenButton))
        if mode.menu==True:
            canvas.create_image(700, 125, image=ImageTk.PhotoImage(mode.DaisyButton))
            canvas.create_image(620, 125, image=ImageTk.PhotoImage(mode.ChloeButton))
        if mode.paused==True:
            canvas.create_text(400, 300, text="PAUSED", font='Arial 40', fill="#302519")
        if mode.gameOver==True:
            canvas.create_image(400,300, image= ImageTk.PhotoImage(mode.GameOverText))
#taken from 15112 website and altered
class HelpMode(Mode):
    def appStarted(mode):
        mode.instruction= mode.loadImage("public/instruction.png")
    def redrawAll(mode, canvas):
        canvas.create_image(400, 300, image=ImageTk.PhotoImage(mode.instruction))

    def mousePressed(mode, event):
        mode.app.setActiveMode(mode.app.gameMode)
class CreditScreen (Mode):
    def appStarted(mode):
        mode.credit=mode.loadImage("public/Credits.png")
    def redrawAll(mode,canvas):
        canvas.create_image(400, 300, image=ImageTk.PhotoImage(mode.credit))
class OptionsScreen(Mode):
    def appStarted(mode):
        mode.options=mode.loadImage("public/OptionsScreen.png")
        mode.minionShortestPath=False
        mode.bgMusic=False
        mode.unlimitedMoney=False
        mode.color=False
        mode.difficulty=4
    def redrawAll(mode,canvas):
        canvas.create_image(400, 300, image=ImageTk.PhotoImage(mode.options))
        if mode.bgMusic==True:
            canvas.create_oval(633-7,156-7,633+7,156+7,fill="white")
        if  mode.minionShortestPath==True:
            canvas.create_oval(633-7,244-7,633+7,244+7, fill="white")
        if mode.unlimitedMoney==True:
            canvas.create_oval(633-7,310-7,633+7,310+7,fill="white")
        if mode.color==True:
            canvas.create_oval(633-7,374-7,633+7,374+7,fill="white")
        if mode.difficulty==1:
            canvas.create_oval(370-14,435-14,370+14,435+14)
        elif mode.difficulty==2:
            canvas.create_oval(456-14,435-14,456+14,435+14)
        elif mode.difficulty==3:
            canvas.create_oval(553-14,435-14,553+14,435+14)   
        elif mode.difficulty==4:
            canvas.create_oval(633-14,435-14,633+14,435+14)   
        elif mode.difficulty==5:
            canvas.create_oval(295-14,435-14,295+14,435+14)  
    def mousePressed(mode, event):
        print(event.x,event.y)
        if event.x>349 and event.x<482 and event.y>486 and event.y<530:
            mode.app.minionShortestPath=mode.minionShortestPath
            mode.app.bgMusic=mode.bgMusic
            mode.app.unlimitedMoney=mode.unlimitedMoney
            mode.app.color=mode.color
            mode.app.difficulty=mode.difficulty
            mode.app.setActiveMode(mode.app.gameMode)
        if event.x>633-10 and event.x<633+10 and event.y>156-10 and event.y<156+10:
            mode.bgMusic=not mode.bgMusic
        if event.x>633-10 and event.x<633+10 and event.y>244-20 and event.y<244+10:
            mode.minionShortestPath= not mode.minionShortestPath
        if event.x>633-10 and event.x<633+10 and event.y>310-20 and event.y<310+10:
            mode.unlimitedMoney= not mode.unlimitedMoney
        if event.x>633-10 and event.x<633+10 and event.y>374-20 and event.y<374+10:
            mode.color= not mode.color
        if event.x>370-7 and event.x<370+7 and event.y>435-7 and event.y<435+7:
            mode.difficulty=1
        if event.x>456-7 and event.x<456+7 and event.y>435-7 and event.y<435+7:
            mode.difficulty=2
        if event.x>553-7 and event.x<553+7 and event.y>435-7 and event.y<435+7:
            mode.difficulty=3
        if event.x>633-7 and event.x<633+7 and event.y>435-7 and event.y<435+7:
            mode.difficulty=4
        if event.x>295-7 and event.x<295+7 and event.y>435-7 and event.y<435+7:
            mode.difficulty=5
#taken from 15112 website and altered
class MyModalApp(ModalApp):
    def appStarted(app):
        app.bgMusic= False
        app.minionShortestPath=False
        app.unlimitedMoney=False
        app.color=False
        app.difficulty=4
        app.splashScreenMode = SplashScreenMode()
        app.gameMode = GameMode()
        app.helpMode = HelpMode()
        app.optionsScreen= OptionsScreen()
        app.creditsPage= CreditScreen()
        app.setActiveMode(app.splashScreenMode)
        app.timerDelay = 50
app = MyModalApp(width=800, height=600)



