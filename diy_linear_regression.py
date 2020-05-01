import matplotlib.pyplot as plt
import numpy as np
size = int(input("size of X:\n"))
X=np.random.randint(low = 0, high = size, size = size) 
w =eval(input("W slope of line:\n"))#1
b =eval(input("B intercept of line:\n"))#0
y = [] 
for x in X:
	y.append(w*x+b)
print(y)
print(X)
plt.plot(X,y ,linewidth=2.0,color="b")
plt.ylabel('some numbers')
plt.show()
