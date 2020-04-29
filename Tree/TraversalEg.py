class Node:
    data = 0
    def __init__(self , val=None):
        self.data = val
        self.left = None
        self.right = None

class Queue:    
    def __init__(self):
        self.queue = []
    def __len__(self):
        return len(self.queue)
    def enqueue(self, val):   
        self.queue.insert(0,val)           
            
    def dequeue(self):       
        return self.queue.pop(len(self.queue) -1)
class Tree:
    root = Node(0)
    cond = False
    def __init__(self , root=None):
        if(root == None):
            self.root = Node(0)
            
            
        else:
            self.root = root
        self.bstroot = None
        self.curr = None
        
    def InOrder(self, node):
        if(node == None):
            return
        self.InOrder(node.left)
        print(node.data ),
        self.InOrder(node.right)
    def PreOrder(self, node):
        if(node == None):
            return
        print(node.data),
        self.PreOrder(node.left)
        self.PreOrder(node.right)
    def PostOrder(self,node):
        if(node == None):
            return
        
        self.PreOrder(node.left)
        self.PreOrder(node.right)
        print(node.data),

    def lvlOrderTraverse(self , root):
        lqueue = Queue()
        lqueue.enqueue(root)
        while(len(lqueue)):
            temp = lqueue.dequeue()
            print(temp.data),
            if(temp.left != None):
                lqueue.enqueue(temp.left)
            if(temp.right != None):
                lqueue.enqueue(temp.right)

        
    def CreateBST(self, val):
        if(self.curr==None):
            self.curr=Node(val)
            print("i am in None")
            return 
        if(self.curr.data > val): # if the current node greater the value, push left
            print("in greater")

            if(self.curr.left == None):
                self.curr.left = Node(val)
                return
            else:
                self.CreateBST(val)
        if(self.curr.data < val):
            print("in lesser")
            if(self.curr.right == None):
                self.curr.right = Node(val)
                return
            else:
                self.CreateBST(val)
    
    def myBST(self, val):  
        if(self.bstroot == self.curr):
            print("No change in value ")
        
        self.CreateBST(val)
        if (self.curr != None ) and (self.cond == False):
            self.bstroot = self.curr
            self.cond = True
        self.curr = self.bstroot
        print(type(self.bstroot))
        print(self.cond)


        broot = self.bstroot
        return broot


root = Node(1) 
root.left      = Node(2) 
root.right     = Node(3) 
root.left.left  = Node(4) 
root.left.right  = Node(5) 
myTree = Tree(root)
print("InOrder \n")
myTree.InOrder(root)
print("\nPreOrder \n")
myTree.PreOrder(root)
print("\nPostOrder \n")
myTree.PostOrder(root)
print("\nBread First Traversal \n")
myTree.lvlOrderTraverse(root)
root = Node()
root = myTree.myBST(10)
root = myTree.myBST(11)
root = myTree.myBST(5)
root = myTree.myBST(12)
root = myTree.myBST(2)
root = myTree.myBST(14)
root = myTree.myBST(4)
myTree.lvlOrderTraverse(root)

