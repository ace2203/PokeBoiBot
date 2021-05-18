import numpy
import random
import math
import time
from operator import add
class pokeboi:
    type=0 #from 0 to 3
    atk=5 
    defense=5 #must sum to 10
    HP=50
    moveHistory=[0,0,0]    
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
        

def BattleWinnerRnd(pok1,pok2):
    
    while pok1.HP >0 and pok2.HP>0:
        move1=random.randint(0,2)
        move2=random.randint(0,2)

        PokeMove(pok1,pok2,move1)
        PokeMove(pok2,pok1,move2)    
        pok1.negativeQ
        pok2.negativeQ

        


battlenum=0
p1WinListRnd=numpy.full(1000,0)

while battlenum<1000:
    pok11=pokeboi(5,5,1)
    pok22=pokeboi(5,5,1)
    
    BattleWinnerRnd(pok11,pok22)
    
    if pok11.HP>0:
            p1WinListRnd[battlenum]=1
    elif pok11.HP==0:
            p1WinListRnd[battlenum]=0
    
    battlenum+=1

p1WinPercentRnd=numpy.sum(p1WinListRnd)/len(p1WinListRnd) 

actionvalue=numpy.load("actionvalue.npy")
battlenum=0

def BattleWinnerAI(pok1,pok2):

    while pok1.HP >0 and pok2.HP>0:
        move1=numpy.argmax(actionvalue[pok1.HP,pok1.atk,pok1.defense])
        
        pok1.moved(move1)

        move2=random.randint(0,2)

        PokeMove(pok1,pok2,move1)
        PokeMove(pok2,pok1,move2)    
        pok1.negativeQ
        pok2.negativeQ
   


p1WinListAI=numpy.full(10000,0)
movesTotal=[0,0,0]
while battlenum<10000:
    pok11=pokeboi(5,5,1)
    pok22=pokeboi(5,5,1)
    
    BattleWinnerAI(pok11,pok22)
    
    movesTotal=list(map(add,movesTotal,pok11.moveHistory))
    
    if pok11.HP>0:
            p1WinListAI[battlenum]=1
    elif pok11.HP==0:
            p1WinListAI[battlenum]=0
    battlenum+=1

p1WinPercentAI=numpy.sum(p1WinListAI)/len(p1WinListAI)
print("random p1 win %:  ",p1WinPercentRnd)
print("AI p1 win %:  ", p1WinPercentAI)
movesTotal=list(map((lambda x, y=sum(movesTotal):x/y),movesTotal))
print("chose %: Kill, Atk, Def",movesTotal)


#is Def really a good move? testing without defense boosts

battlenum=0

def BattleWinnerAINoDef(pok1,pok2):

    while pok1.HP >0 and pok2.HP>0:
        move1=numpy.argmax(actionvalue[pok1.HP,pok1.atk,pok1.defense])
       
        if move1>1:
          # move1=random.randint(0,1)
            temp=random.randint(0,2)
            if temp<2:
                move1=0
            else:
                move1=1
        
        pok1.moved(move1)

        move2=random.randint(0,2)

        PokeMove(pok1,pok2,move1)
        PokeMove(pok2,pok1,move2)    
        pok1.negativeQ
        pok2.negativeQ

p1WinCounterAINoDef=0
movesTotalNoDef=[0,0,0]

while battlenum<10000:
    pok11=pokeboi(5,5,1)
    pok22=pokeboi(5,5,1)
    
    BattleWinnerAINoDef(pok11,pok22)
    
    movesTotalNoDef=list(map(add,movesTotalNoDef,pok11.moveHistory))
    
    if pok11.HP>0:
            p1WinCounterAINoDef+=1
    battlenum+=1

print("AI w/0 def win %", p1WinCounterAINoDef/battlenum)
movesTotalNoDef=list(map((lambda x, y=sum(movesTotalNoDef):x/y),movesTotalNoDef))
print("confirm no def", movesTotalNoDef) #boosting the defense is really important!