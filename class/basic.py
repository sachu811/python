class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def persondetails(self):
        print(self.name)
        print(self.age)

persondetails=Person('sachu','25')
persondetails.persondetails()

class Person1:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"{self.name} {self.age}"
P1=Person1('sachin',33)
print(P1)