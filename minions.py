from cmu_112_graphics import *
def getCell(x,y):
    #top left
    x0=x-43//2
    y0=y-50//2

    #bottom right
    x3=x+43//2
    y3=y+50//2
    return (x//50-1, y//50-1)


class Minion(object):
    def __init__(self,startY):
        self.cx=50
        self.cy=50+startY*50
        self.direction="right"
        self.speed=3
        self.i=0
    def calculateNextDir(self, L):
        (col,row)= getCell(self.cx, self.cy)
        moves=[(1,0),(-1,0), (0,-1), (0,1)]
        for move in moves:
            if row+move[0] >=0 and col+move[1]>=0 and row+move[0] < len(L) and col+move[1]<len(L[0]) and L[row+move[0]][col+move[1]]>0 and  L[row+move[0]][col+move[1]]>L[row][col]:
                return move
        return (0,0)
class CrabMinion(Minion):
    def __init__(self,startY):
        super().__init__(startY)
        self.speed=4

