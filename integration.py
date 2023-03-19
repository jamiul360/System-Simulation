import random
import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return x**3


x = []
y = []

i=0
h=0.2
while i<1000:
    val = i
    x.append(val)
    y.append(func(val))
    i += h



plt.plot(x,y)
#plt.show()


n=0
m=0
for i in range(500):

    rx = random.randint(20,50)
    rx = rx/10
    ry = random.randint(0,200)
    if ry<=func(rx):
        m+=1
    n+=1

    plt.scatter(rx,ry)

#plt.show()

print(m)
area = (m/n)*(3*200)
print(area)
