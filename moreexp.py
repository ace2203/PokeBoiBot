import numpy as np
a=np.full((1,4),3)
print(type(a))
if type(a) is np.ndarray:
    print("works")