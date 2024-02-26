class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linklist:
    def __init__(self):
        self.head=None
    
    def insert(self,value):
        newVal=Node(value)
        if(self.head==None):
            self.head=newVal
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=newVal
    
    def print(self):
        if(self.head==None):
            print("empty list")
        else:
            temp=self.head
            while(temp!=None):
                print(temp.data,end="")
                temp=temp.next
    def delete(self):
        if(self.head==None):
            print("empty link")
        else:
            self.head=self.head.next


list=Linklist()
list.insert(1)
list.insert(2)
list.insert(3)
list.print()
list.delete()
print()
list.print()