import matplotlib.pyplot as plt
import numpy as np
x=[0,2,4,6,8]
y=[10,20,60,70,100]
font1={'family':'serif','color':'blue'}
plt.xlabel("Time",fontdict=font1)
plt.ylabel("Speed",fontdict=font1)
plt.title("Car Speed",fontdict=font1)
plt.plot(x,y,marker='o')
plt.show()