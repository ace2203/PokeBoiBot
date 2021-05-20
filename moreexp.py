import numpy
actionvalue=numpy.load("actionvalue.npy")
print(actionvalue[25,5,5,1])
a=[[1,2,3],[4,5,6],[7,8,9]]
print (a[:3])
print(isinstance(actionvalue,numpy.ndarray)) 