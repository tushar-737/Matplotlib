import matplotlib.pyplot as plt
import numpy as np
salary=np.array([50000,40000,45000,69000,20000,36000,39000])
plt.hist(salary,bins=4,color='red')
plt.show()