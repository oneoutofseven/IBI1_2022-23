#aim: calculating the generation needed to reach 100 rabbits
#initial number of rabbit: 2, a couple can breed two rabbits
#while() is needed

g=1
n=2
while n<100:
  n=2*n
  g=g+1

print ("At %d generation over 100 rabbits have been born" % g)



