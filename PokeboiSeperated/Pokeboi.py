import numpy
import random
import math
import matplotlib.pyplot as plt
from operator import add

class pokeboi:
    type=0 #from 0 to 3
    atk=5 
    defense=5 #must sum to 10
    HP=50
    moveHistory=[0,0,0]
    moveHistoryTime=numpy.full((300,3),0)
    stateHistory=numpy.full((300,4),0)
    battlenum=0
    typeChart=[[1,.5,0,2],[2,1,.5,0],[0,2,1,.5],[.5,0,2,1]]
    
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
        self.stateHistory=numpy.full((300,4),0)       

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
       self.stateHistory[self.battlenum]=[self.HP,self.atk,self.defense,moveNum]
       self.battlenum+=1
      
    
    def moveReset(self):
        self.moveHistory=[0,0,0]

def DamCalc( atkPok, defnPok):
    return math.ceil(atkPok.typeChart[atkPok.type][defnPok.type]*atkPok.atk/defnPok.defense)

def PokeMove(atkPok,defnPok,moveNum):
    if moveNum==0:
        defnPok.hit(DamCalc(atkPok,defnPok))
    if moveNum==1:
        atkPok.addAtk()
    if moveNum==2:
        atkPok.addDefn()


def BattleWinnerAI(pok1,AI1,pok2,AI2):

    while pok1.HP >0 and pok2.HP>0:
        if AI1 is numpy.ndarray:
            move1=numpy.argmax(AI1[pok1.HP,pok1.atk,pok1.defense])
        else:
            move1=random.randint(0,2)
        
        pok1.moved(move1)

        if AI2 is numpy.ndarray:
            move2=numpy.argmax(AI1[pok1.HP,pok1.atk,pok1.defense])
        else:
            move2=random.randint(0,2)

        PokeMove(pok1,pok2,move1)
        PokeMove(pok2,pok1,move2)    
        pok1.negativeQ
        pok2.negativeQ
