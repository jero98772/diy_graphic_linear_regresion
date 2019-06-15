import matplotlib.pyplot as plt
import numpy as np

x=np.array([-2,-1,0,1,2])
w =eval(input("W pending of line:\n"))
b =eval(input("B intercept of line:\n"))
#for x in x:
y=w*x+b
plt.plot(y ,linewidth=2.0)
plt.ylabel('some numbers')
plt.show()