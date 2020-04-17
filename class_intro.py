class vinClass:
    """ My class intro """
    f = 3
    def __init__(self):
        self.f +=23
    def inVinFunc(self):
        print("inside inVinFunc")
        print(self.f)
    def setFunc(self ,a):
        self.f +=a
        print(self.f)

class Node:
    def __init__(self , data=None):
        self.data = data
        self.next = None
class LList:
    tail = Node()
    headval = Node()
    headval =None
    def __init__(self):
        self.headval = None
    def add_node(self, val):
        newnode = Node(val) #create a node each time the function add_node is getting called 
        # assign a value that is passed 
        if(self.headval == None ):
            self.headval = newnode # point the head pointer to the newnode that is created
            # create a tail node to point to the last node. Else you will have to traverse all the 
            # to find out the end of the node to add a new node
            self.tail = newnode
        else:
            self.tail.next = newnode
            self.tail = newnode
    def traverseNode(self):
        printval = self.headval
        while printval is not None:
            print(printval.data)
            printval = printval.next
    

l1 = LList()
l1.add_node(1)
l1.add_node(2)
l1.add_node(3)
l1.add_node(4)
l1.traverseNode()

x = vinClass()
x.setFunc(5)
print(x.__doc__)
