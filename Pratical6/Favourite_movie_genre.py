tinydict = {"Comedy":73,"Action":42,"Romance":38,"Fantasy":28,"Science-fiction":22,"Horror":19,"Crime":18,"Documentary":12,"History":8,"War":7}
#create the dictionary of "favourite movie genre"

import matplotlib.pyplot as plt
import numpy as np

requested_genre = "Comedy"

print ("The number of students who prefer", requested_genre, "is :",tinydict[requested_genre])

labels=tinydict.keys() #genre
y = tinydict.values() #the data

plt.pie(y,labels=labels,autopct="%d%%")
plt.title("Favourite movie genre") #title of the chart
plt.show()
        
 
