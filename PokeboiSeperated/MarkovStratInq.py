from os import O_TEMPORARY
import numpy
import random
import math
import time
import matplotlib.pyplot as plt
from operator import add
import importlib.util

from numpy.matrixlib.defmatrix import bmat
spec = importlib.util.spec_from_file_location("Pokeboi.py", "C:/Users/W. Baker/OneDrive/Documents/GitHub/PokeBoiBot/PokeboiSeperated/Pokeboi.py")
pb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pb)

def dMove (move):
    temp=numpy.full(numpy.shape(move),0)
   
    for i in range(len(move)-1):
        temp[i]=move[i+1]-move[i]
    for i in range(100):
       for j in range(3):
           if temp[i,j]<0:
               temp[i,j]=0
    return temp

actionvalue=numpy.load("actionvalue.npy")
moveHistoryTotal=numpy.full((100,3),0)
bnH=numpy.full(100,0)
winCounter=0
battleCounter=0
while battleCounter<100:

    pok11=pb.pokeboi(5,5,1)
    pok22=pb.pokeboi(5,5,1)
    pb.BattleWinnerAI(pok11,actionvalue,pok22,False)
    moveHistoryTotal=numpy.add(moveHistoryTotal,dMove(pok11.moveHistoryTime))
    bnH[battleCounter]=pok11.battlenum
    battleCounter+=1
    if pok11.HP>0:
        winCounter+=1
#elif pok11.HP==0:
#        print("AI lost")
print(bnH)
print(winCounter/battleCounter*100)
print(numpy.shape(pok11.moveHistoryTime))
xt=numpy.linspace(0,20,dtype=int)
y1=moveHistoryTotal[xt, 0]
y2=moveHistoryTotal[xt, 1]
y3=moveHistoryTotal[xt, 2]
y4=numpy.add(numpy.add(y2,y1),y3)

plt.plot(xt,y1,label="Kill")
plt.plot(xt,y2,label="Atk")
plt.plot(xt,y3,label="Def")
plt.plot(xt,y4,label="total")

plt.xlabel("round #")
plt.ylabel("freq")
plt.legend()
plt.show()

#print(pok11.moveHistoryTime[0:20])
#xT=numpy.linspace(0,pok11.battlenum,dtype=int)
#y1=pok11.moveHistoryTime[xT, 0]
#y2=pok11.moveHistoryTime[xT, 1]
#y3=pok11.moveHistoryTime[xT, 2]

#fig, (ax1,ax2,ax3) = plt.subplots(3,1)
#fig.suptitle("Move vs Time")

#ax1.plot(xT,y1)
#ax1.set_ylabel("Kill")

#ax2.plot(xT,y2)
#ax2.set_ylabel("Atk buff")

#ax3.plot(xT,y3)
#ax3.set_ylabel("Def buff")

#plt.show()