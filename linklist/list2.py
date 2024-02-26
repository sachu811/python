class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

node1=Node(1)
node2=Node(2)
node3=Node(3)
node4=Node(4)
node5=Node(5)

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
node5.next=node1

if node1.next is node2:
    print("Yes ! node1 next store node2 reference")
print(node3.next.data)
