import numpy as np
import math

import matplotlib.pyplot as plt

x=np.linspace(0.1 , 500 , 1000)

# y=[1/(1+np.exp(-i)) for i in x]   #sigmoid

y=[math.log(i,2) for i in x]
y2=[math.log(i,4) for i in x]

plt.plot(x,y)
plt.plot(x,y2)

plt.show()