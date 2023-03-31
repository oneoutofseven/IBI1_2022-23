import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#correct code for showing the second column from every 100th row from the first 1000 rows
df = pd.read_csv("full_data.csv")
df.iloc[0:1100:100,1] #list the numbers
print (df.iloc[0:1100:100,1])

#a Boolean to show “total cases” for all rows corresponding to Afghanistan
is_Afghanistan= df["location"]=="Afghanistan" #Boolean distinguish
print (df.loc[df["location"]=="Afghanistan","total_cases"])

# mean number of new cases and new deaths on 31 March 2020
newcases = df.loc[df.date=="2020-03-31","new_cases"] #make a dataframe of the new cases on 2020-03-31
newdeaths = df.loc[df.date=="2020-03-31","new_deaths"] #make a dataframe of the new deaths on 2020-03-31
print (newcases)
print ("Mean Number of New Cases on 2020-03-31 is", np.mean(newcases)) #caculate the mean
print (newdeaths)
print ("Mean Number of New Deaths on 2020-03-31 is", np.mean(newdeaths))

#boxplot of new cases and new deaths on 31 March 2020
world_data= df.loc[df.date=="2020-03-31",["new_cases","new_deaths"]]
print (world_data)
plt.boxplot([world_data.iloc[:,0],world_data.iloc[:,1]],labels=['new_cases','new_deaths']) #make the boxplot 
plt.title("world data on 2020-03-31")
plt.ylabel("population")
plt.show()

# plot both new cases and new deaths worldwide over time
x = df.loc[df.location=="World", "date"]
y = df.loc[df.location == "World", "new_cases"]
plt.figure(figsize=(10,10)) # adjust the size of the picture
plt.plot(x, y, "b+")
plt.xticks(x.iloc[0:len(x):4], rotation=-90)  #make an interval of 4 for "date" to make the "date" not too tight
plt.title("new cases worldwide over time")
plt.ylabel("population")
plt.show()

x = df.loc[df.location=="World", "date"]
y = df.loc[df.location == "World", "new_deaths"]
plt.figure(figsize=(10,10))
plt.plot(x, y, "b+")
plt.xticks(x.iloc[0:len(x):4], rotation=-90)
plt.title("new cases worldwide over time")
plt.ylabel("population")
plt.show()

# Question to answer
x = df.loc[df.location=="Germany", "date"]
y = df.loc[df.location == "Germany", "new_cases"]
plt.figure(figsize=(10,10)) # adjust the size of the picture
plt.plot(x, y, "b+")
plt.xticks(x.iloc[0:len(x):4], rotation=-90)  #make an interval of 4 for "date" to make the "date" not too tight
plt.title("new cases in Germany over time")
plt.ylabel("population")
plt.show()

x = df.loc[df.location=="Germany", "date"]
y = df.loc[df.location == "Germany", "total_cases"]
plt.figure(figsize=(10,10))
plt.plot(x, y, "b+")
plt.xticks(x.iloc[0:len(x):4], rotation=-90)
plt.title("total cases in Germany over time")
plt.ylabel("population")
plt.show()


