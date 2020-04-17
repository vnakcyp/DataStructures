#Binary search treee implmenation

class Node:
    def __init__(self ,data = None):
        self.left = None
        self.right = None
        self.data = data
class Tree:
    #traverse = Node(0)
    root = Node(0)
    def __init__(self, val):
        self.root.data = val
        #self.traverse = self.root
    def recurse_add(self, cnode ,data):    
        print("the data in cnode is",cnode.data)   
        print("the data received is", data) 
        if(data > cnode.data ):
            if(cnode.right  == None):
                cnode.right = Node(data)
                return
            else:
                self.recurse_add(cnode.right, data)
                return
        if(data < cnode.data):
            if(cnode.left == None):
                cnode.left = Node(data)
                return
            else:
                self.recurse_add(cnode.left ,data)
                return
    
    def Tprint(self,traverse):
        if traverse.left:
            self.Tprint(traverse.left)
        
        if traverse.right:
            self.Tprint(traverse.right)
        print(traverse.data)
    def searchelper(self, snode , val):

        if(val > snode.data):
            if snode.left == None:
                return False
            
            return (self.searchelper(snode.right , val ))
        elif(val ==  snode.data):
            print("found you ")
            return True
            
        else:
            return (self.searchelper(snode.left , val ))

    def serachVal(self, val):
        if(searchelper(self.root, val)):
            print("present in the tree")
            return True
        else:
            print("Not present in the tree")
            return False
    def PrintTree(self):
        self.Tprint(self.root)                     
           
    def add_Node(self,nodeval):
        self.recurse_add(self.root, nodeval)

       
m = Tree(10)
m.add_Node(3)  
m.add_Node(5)
m.add_Node(11)
m.add_Node(15)
m.add_Node(2)
m.PrintTree()

