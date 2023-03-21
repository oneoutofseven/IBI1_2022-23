import matplotlib.pyplot as plt
import numpy as np

c=[1,8,15,7,5,14,43,40]  #costs list
costs=sorted(c)
print (costs)

x = np.array(["Los Angeles 1984", "Sydney 2000", "Atlanta 1996", "Seoul 1988", "Athens 2004", "Barcelona 1992", "London 2012", "Beijing 2008"])
y = np.array(costs)

plt.barh(x,y)  #form the bar chart
plt.show()
