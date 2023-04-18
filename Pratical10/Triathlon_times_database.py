class Triathlon(object):
    def __init__(self,f,la,lo,s,c,r):
      self.first_name = f
      self.last_name = la
      self.location = lo
      self.swim = s
      self.cycle = c
      self.run = r
      self.total = s+c+r
    def speak(self):
      print("%s %s location:%s swim:%d hours  cycle:%d hours  run:%d hours  total time:%d hours" %(self.first_name,self.last_name,self.location,self.swim,self.cycle,self.run,self.total))

p = Triathlon("Chenzhi","Xu","Haining",3,3,3)
p.speak()
