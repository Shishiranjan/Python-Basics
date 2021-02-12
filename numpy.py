import matplotlib.pyplot as plt
import numpy as np

x, y = np.loadtxt('Employee.txt', delimiter = ',', unpack = True)

plt.plot(x, y, label = 'Loaded from file')
plt.xlabel('Plot number')
plt.ylabel('Randomly chosen number')
plt.legend()
plt.title('Awesome graph')
plt.show()
