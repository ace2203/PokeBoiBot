import numpy
import random
import math
import time
import matplotlib.pyplot as plt
from operator import add
class pokeboi:
    type=0 #from 0 to 3
    atk=5 
    defense=5 #must sum to 10
    HP=50
    moveHistory=[0,0,0]
    moveHistoryTime=numpy.full((300,3),0)
    battlenum=0
    def __init__(self,atkN,defN,typeN):
        self.atk=atkN
        self.defense=defN
        if self.atk+self.defense>10:
            self.atk=5
            self.defense=5
            print("invalid stat configuraiton")
        self.type=typeN
        if typeN>3:
            self.type=0
        self.moveHistory=[0,0,0]
        self.battlenum=0       

    def StatConfig(self,atkN,defenseN):
        self.atk=atkN
        self.defense=defenseN

    def TypeConfig(self,typeN):
        self.type=typeN
        if typeN>3:
            self.type=0

    def hit(self,hitv):
        self.HP=self.HP-hitv #hitv is positive for health loss, negative for health gain

    def addAtk(self):
        if self.atk<51:
            self.atk=self.atk+1

    def addDefn(self):
        if self.defense<51:
            self.defense=self.defense+1
    def negativeQ(self):
        if self.HP<0:
            self.HP=0
    def moved(self,moveNum):
       self.moveHistory[moveNum]+=1
       self.moveHistoryTime[self.battlenum]=self.moveHistory
       self.battlenum+=1
    
    def moveReset(self):
        self.moveHistory=[0,0,0]
   

typeChart=[[1,.5,0,2],[2,1,.5,0],[0,2,1,.5],[.5,0,2,1]]

def DamCalc( atkPok, defnPok):
    return math.ceil(typeChart[atkPok.type][defnPok.type]*atkPok.atk/defnPok.defense)

def PokeMove(atkPok,defnPok,moveNum):
    if moveNum==0:
        defnPok.hit(DamCalc(atkPok,defnPok))
    if moveNum==1:
        atkPok.addAtk()
    if moveNum==2:
        atkPok.addDefn()

actionvalue=numpy.load("actionvalue.npy")

def BattleWinnerAI(pok1,pok2):

    while pok1.HP >0 and pok2.HP>0:
        move1=numpy.argmax(actionvalue[pok1.HP,pok1.atk,pok1.defense])
        
        pok1.moved(move1)

        move2=random.randint(0,2)

        PokeMove(pok1,pok2,move1)
        PokeMove(pok2,pok1,0)    
        pok1.negativeQ
        pok2.negativeQ
   


pok11=pokeboi(5,5,1)
pok22=pokeboi(5,5,1)
    
BattleWinnerAI(pok11,pok22)
    
   
    
if pok11.HP>0:
        print("AI won")
elif pok11.HP==0:
        print("AI lost")
    
xT=numpy.linspace(0,pok11.battlenum,dtype=int)
y1=pok11.moveHistoryTime[xT, 0]
y2=pok11.moveHistoryTime[xT, 1]
y3=pok11.moveHistoryTime[xT, 2]

fig, (ax1,ax2,ax3) = plt.subplots(3,1)
fig.suptitle("Move vs Time")

ax1.plot(xT,y1)
ax1.set_ylabel("Kill")

ax2.plot(xT,y2)
ax2.set_ylabel("Atk buff")

ax3.plot(xT,y3)
ax3.set_ylabel("Def buff")

plt.show()