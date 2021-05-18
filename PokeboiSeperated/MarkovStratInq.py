import numpy
import random
import math
import matplotlib.pyplot as plt
from operator import add
import importlib.util
spec = importlib.util.spec_from_file_location("Pokeboi.py", "C:/Users/W. Baker/OneDrive/Documents/GitHub/PokeBoiBot/PokeboiSeperated/Pokeboi.py")
pb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pb)



actionvalue=numpy.load("actionvalue.npy")

winCounter=0
battleCounter=0
while battleCounter<1000:

    pok11=pb.pokeboi(5,5,1)
    pok22=pb.pokeboi(5,5,1)
    
    pb.BattleWinnerAI(pok11,actionvalue,pok22,actionvalue)
    battleCounter+=1
    if pok11.HP>0:
        winCounter+=1
#elif pok11.HP==0:
#        print("AI lost")
print(winCounter/battleCounter*100)
print(pok11.moveHistoryTime[0:20])
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