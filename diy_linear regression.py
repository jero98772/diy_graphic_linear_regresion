import matplotlib.pyplot as plt
import numpy as np

X=[
8,8,7,8,7,8,8,8,8,8,8,7,8,8,
7,8,9,7,8,7.2,7.2,7,4,7,6,7,8,7,7,7]#example data
x=np.array(X)
w =eval(input("W pending of line:\n"))#1
b =eval(input("B intercept of line:\n"))#0

y=w*x+b

plt.plot(X ,'ro',linewidth=2.0)

plt.plot(y ,linewidth=2.0)
plt.ylabel('some numbers')
plt.show()
