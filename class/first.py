class SS:
  def __init__(self,fname,lname):
    self.name=fname+' '+lname
  def show(self):
    print(self.name)
  
test=SS('Me','Mine')
test.show()


class NS:
  def __init__(self,Me,Mycar):
    self.Me=Me
    self.Mycar=Mycar

  def show(self):
    print(self.Me+' '+self.Mycar)

  def __str__(self):
    return f"{self.Me} owner car {self.Mycar}"
  

    
  
test1=NS('raj','ambasder')
test1.show()
print(test1)
# return
# print()