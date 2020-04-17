class Node:
    def __init__(self ,data = None):
        self.left = None
        self.right = None
        self.data = data
class Queue:    
    def __init__(self):
        self.queue = []
    def __len__(self):
        return len(self.queue)
    def enqueue(self, val):   
        self.queue.insert(0,val)           
            
    def dequeue(self):       
        return self.queue.pop(len(self.queue) -1)
#create a list of additions in the heap
#append the new value in the back of the list
#adjust the heap accordingly to fit in the new element
#finally do a level traversal to add the Node in the final heap created

class MyHeap:
    heap = Node()
    def __init__(self):
        heap = None
    def addNode(self, val):
        cnode = Node(val)
        lqueue = Queue()
        lqueue.enqueue(cnode)
        if( )
        
    def addToHeap():        
        while(len(lqueue)):
            MyNode = lqueue.dequeue()
            if(len(lqueue)):
                lqueue.enqueue(cnode)
        
