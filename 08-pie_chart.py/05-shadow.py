import matplotlib.pyplot as plt
import numpy as np
x=np.array([20,30,25,25])
y=np.array(['1','2','3','4'])
explode=[0.2,0,0,0]
plt.pie(x,labels=y,explode=explode,shadow=True)
plt.show()