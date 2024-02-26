class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


#create two nodes
node1=Node(1)
node2=Node(2)

#link the node together
node1.next=node2

# Print node1's next attribute (which is a reference to node2)
print(node1.next)

#print value
print(node1.next.data)