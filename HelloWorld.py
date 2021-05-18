import matplotlib.pyplot as plt
import numpy as np
from numpy.core.fromnumeric import choose

#x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
#plt.plot(x, np.sin(x))       # Plot the sine of each x point
#plt.show()                   # Display the plot

actionvalue=np.load("actionvalue.npy")

#avt=np.full((10,10,3),1)

dim=52*52*52

actionvalueflat=np.reshape(actionvalue,(dim,3))
#actionvalueflat=np.array([[1,2,3],[4,5,6]])

chooseDef=0
chooseAtk=0
chooseKill=0
wtf=0
for moves in actionvalueflat:
    if moves[2]>moves[1] and moves[2]> moves[0]:
        chooseDef+=1
    elif moves[1]>moves[2] and moves[1]>moves[0]:
        chooseAtk+=1
    elif moves[0]>moves[1] and moves[0]> moves[2]:
        chooseKill+=1
    else:
        wtf+=1
uniqueChoice=chooseKill+chooseAtk+chooseDef

print(chooseKill/uniqueChoice)
print(chooseAtk/uniqueChoice)        
print(chooseDef/uniqueChoice)
