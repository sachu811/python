class Inharit:
  def __init__(self,company,type):
    self.company=company
    self.type=type

  def show(self):
    print("Hello")

inharit=Inharit('Tata','still')
# inharit.show()

class Employee(Inharit):
  def __init__(self,name,roll):
    self.name=name
    self.roll=roll
  
  def show(self):
    print(self.name+' '+self.roll)
  
  def showc(self):
    super().show()
  
employ=Employee('Raja','123')
employ.show()
employ.showc()
