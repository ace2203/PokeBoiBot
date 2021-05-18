import numpy
import random
import math
import matplotlib.pyplot as plt
from operator import add
import importlib.util
spec = importlib.util.spec_from_file_location("Pokeboi.py", "C:/Users/W. Baker/OneDrive/Documents/GitHub/PokeBoiBot/PokeboiSeperated/Pokeboi.py")
pb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pb)

pok11=pb.pokeboi(5,5,1)
pok22=pb.pokeboi(5,5,1)
tieCounter=0
actionvalue2=numpy.load("actionvalue.npy")
lc=.05
win1Counter=0
win2Counter=0
battleCounter=0
while battleCounter<10000000:

    pok11=pb.pokeboi(5,5,1)
    pok22=pb.pokeboi(5,5,1)
    
    pb.BattleWinnerAI(pok11,actionvalue2,pok22,actionvalue2)
    battleCounter+=1
    if pok11.HP>0:
        win1Counter+=1
        for (i,j,k,l) in pok11.stateHistory[0: pok11.battlenum]:
            actionvalue2[i,j,k,l]+=lc
        for (i,j,k,l) in pok22.stateHistory[0: pok22.battlenum]:
            actionvalue2[i,j,k,l]-=lc
    elif pok22.HP>0:
        win2Counter+=1
        for (i,j,k,l) in pok11.stateHistory[0: pok11.battlenum]:
            actionvalue2[i,j,k,l]-=lc
        for (i,j,k,l) in pok22.stateHistory[0: pok22.battlenum]:
            actionvalue2[i,j,k,l]+=lc
    elif pok22.HP==0 and pok11.HP==0:
            tieCounter+=1
print("AI1 win%: ",win1Counter/battleCounter*100)
print("AI2 win%: ",win2Counter/battleCounter*100)
print("tie %: ",tieCounter/battleCounter*100)
print("1? ",win2Counter/battleCounter*100+win1Counter/battleCounter*100+tieCounter/battleCounter*100)
numpy.save("actionvalue2.npy",actionvalue2, False)