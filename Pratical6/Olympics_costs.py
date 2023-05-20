import matplotlib.pyplot as plt
import numpy as np

d={"Los Angeles 1984":1,"Seoul 1988":8,"Barcelona 1992":15,"Atlanta 1996":7,"Sydney 2000":5,"Athens 2004":14,"Beijing 2008":43,"London 2012":40}
print(d)

c=[1,8,15,7,5,14,43,40]  #costs list
costs=sorted(c)
print (costs)

D=sorted(d.items(),key = lambda x:x[1],reverse=False) #arrange the cities corresponding to "cost" list
city_costs=dict(D)
city=list(city_costs.keys())
x = np.array(city)
y = np.array(costs)

plt.title("costs of the Olympics")
plt.ylabel("costs/$billions")
plt.bar(x,y)  #form the bar chart
plt.xticks(x,rotation=-60)
plt.show()
