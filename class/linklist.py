class Node:
  def __init__(self,data,next=None):
    self.data=data
    self.next=None

class SLL:
  def __init__(self,head=None):
    self.head=head

  def is_empty(self):
    return self.head==None
  
  def insert_data(self,data):
    n=Node(data,self.head)
    self.head=n
  
  def insert_last_node(self,data):
    n=Node(data)
    if not self.is_empty():
      temp=self.head
      while temp.next is not None:
        temp=temp.next
       
      temp.next=n
    else:
      self.start=n
  
  def search(self,data):
    temp=self.head
    while temp is not None:
      if temp.data==data:
        return temp
        
      temp=temp.next
    return None
  

  def insert_after(self,temp,data):
    
    if temp.next is not None:
      n=Node(data,temp.next)
      temp.next=n

  def print(self):
    temp=self.head
    while temp is not None:
      print(temp.data,end='')
      temp=temp.next
      print()
      

link=SLL() 
link.insert_data(2)
link.insert_last_node(3)
link.insert_last_node(4)
# link.print()

# search=link.search(2)
# print(search)
link.insert_after(link.search(3),6)
link.print()


