import matplotlib.pyplot as plt
import numpy as np
x=np.array([20,30,25,25])
y=np.array(['1','2','3','4'])
plt.pie(x,labels=y,startangle=90)
plt.show()