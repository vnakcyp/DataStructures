#level_order traversal

class Queue:    
    def __init__(self):
        self.queue = []
    def __len__(self):
        return len(self.queue)
    def enqueue(self, val):   
        self.queue.insert(0,val)           
            
    def dequeue(self):       
        return self.queue.pop(len(self.queue) -1)


class Node:
    def __init__(self ,data = None):
        self.left = None
        self.right = None
        self.data = data
class Tree:
    lqueue = Queue()
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
        print(traverse.data)     
        if traverse.right:
            self.Tprint(traverse.right)
        print(traverse.data)

    def PrintTree(self):
        self.Tprint(self.root)                     
           
    def add_Node(self,nodeval):
        self.recurse_add(self.root, nodeval)

    def lvlOrderTraverse(self):
        lqueue = Queue()
        lqueue.enqueue(self.root)
        while(len(lqueue)):
            temp = lqueue.dequeue()
            print(temp.data)
            if(temp.left != None):
                lqueue.enqueue(temp.left)
                print(temp.data)
            if(temp.right != None):
                lqueue.enqueue(temp.right)
            
                
class Heap:
    hqueue = []
    def __init__(self ,lst):
        self.hqueue = lst
    
    def heapify(self):
        for i in range(len(self.hqueue)):
            j = i/2
            for j in range(len(self.hqueue)):
                if(self.hqueue[i] > self.hqueue[j]):
                    self.hqueue[i] , self.hqueue[j] = self.hqueue[j] , self.hqueue[i]
                j = j/2               
        self.hqueue


        


        
m = Tree(10)
m.add_Node(3)  
m.add_Node(5)
m.add_Node(11)
m.add_Node(15)
m.add_Node(2)
m.add_Node(51)
m.add_Node(12)
m.lvlOrderTraverse()