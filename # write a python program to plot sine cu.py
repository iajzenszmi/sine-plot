  # write a python program to plot sine curve   
import numpy as nm
import matplotlib as mp
import matplotlib.pyplot as plt     
x=nm.arange(0,4*nm.pi,0.1)
y=nm.sin(x)
plt.title("sine wave form")     
plt.plot(x,y)
plt.show()


