import numpy
import random
import math
import time
import matplotlib.pyplot as plt
from operator import add
import importlib.util
spec = importlib.util.spec_from_file_location("Pokeboi.py", "C:/Users/W. Baker/OneDrive/Documents/GitHub/PokeBoiBot/PokeboiSeperated/Pokeboi.py")
pb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pb)

pok11=pb.pokeboi(5,5,1)
pok22=pb.pokeboi(5,5,1)
tieCounter=0
actionvalue=numpy.full((26,21,21,3),1.0)
#actionvalue2=numpy.load("actionvalue.npy")
#actionvalue3=numpy.full((52,52,52,3),1)
lc=.05
win1Counter=0
win2Counter=0
battleCounter=0
battleRoundAve=0
battleCounterLimit=1000000
startTime=time.perf_counter()
while battleCounter<battleCounterLimit:

    pok11=pb.pokeboi(5,5,1)
    pok22=pb.pokeboi(5,5,1)
    
    pb.BattleWinnerAI(pok11,5,pok22,5)
    battleRoundAve+=pok11.battlenum/battleCounterLimit
    
    battleCounter+=1
    #print("player 1 hp ",pok11.HP,"player 2 hp ",pok22.HP)
    if pok11.HP>0:
        win1Counter+=1
        for (i,j,k,l) in pok11.stateHistory[: pok11.battlenum]:
            actionvalue[i,j,k,l]+=lc
        for (i,j,k,l) in pok22.stateHistory[: pok22.battlenum]:
            actionvalue[i,j,k,l]-=lc
    elif pok22.HP>0:
        win2Counter+=1
        for (i,j,k,l) in pok11.stateHistory[: pok11.battlenum]:
            actionvalue[i,j,k,l]-=lc
        for (i,j,k,l) in pok22.stateHistory[: pok22.battlenum]:
            actionvalue[i,j,k,l]+=lc
    elif pok22.HP<1 and pok11.HP<1:
            tieCounter+=1
    #print("win couts: ",win1Counter, " , ", win2Counter)
endTime=time.perf_counter()
#print(pok11.stateHistory[:pok11.battlenum])
#print(pok22.stateHistory[:pok22.battlenum])
print(actionvalue[25,5,5])
print("AI1 win%: ",win1Counter/battleCounter*100)
print("AI2 win%: ",win2Counter/battleCounter*100)
print("tie %: ",tieCounter/battleCounter*100)
print("1? ",win2Counter/battleCounter*100+win1Counter/battleCounter*100+tieCounter/battleCounter*100)
print("Battle Round Average ", battleRoundAve)
print(endTime-startTime)
numpy.save("actionvalue.npy",actionvalue, False)