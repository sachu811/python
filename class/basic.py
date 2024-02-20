class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def persondetails(self):
        print(self.name)
        print(self.age)

persondetails=Person('sachu','25')
persondetails.persondetails()