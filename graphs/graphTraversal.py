# graph traversal DFT and BFT
import copy
class Queue:    
    def __init__(self):
        self.queue = []
    def __len__(self):
        return len(self.queue)
    def enqueue(self, val):   
        self.queue.insert(0,val)           
            
    def dequeue(self):       
        return self.queue.pop(len(self.queue) -1)
class myStack:
    mystackl = []
    def __init__(self):
        self.mystackl = []
    def __len__(self):
        return len(self.mystackl)
    def push(self, val):
        self.mystackl.append(val)
    def pop(self):       
        val = self.mystackl.pop()
        return val
    def check(self):
        arr = self.mystackl
        l = len(arr)
        return arr[l-1]

class graphs:    
    glist = {}
    def __init__(self):
        self.glist = {}
    def keyChecker(self, key):
        for vrtx in self.glist:
            if( vrtx == key[0]):
                return True
        return False
                
    def addVertex(self, pnode):

        if ((self.keyChecker(pnode.keys()))==False):
            self.glist.update(pnode)
            print("vertex added")
        else:
            print("vertex already present in the graph")
    def addEdge(self):
        edgecol = []    
        for vrtx in self.glist:
            for nvrtx in self.glist[vrtx]:
                if {nvrtx , vrtx} not in edgecol:
                    # use sets to represent edges since the order doesn't matter in sets.
                    edgecol.append({nvrtx , vrtx}) 
                    
    def isvisited(self,arr1, arr2): 
        carr1 = copy.deepcopy(arr1)
        carr2 = copy.deepcopy(arr2)
        carr1.sort()
        carr2.sort()
        if carr1 == carr2:
            return 1
        else:
            return 0

    def BFT(self,start_node):
        Q = Queue()
        Q.enqueue(start_node)
        check_list = []
        for vertex in self.glist:
            v = Q.dequeue()
            check_list.append(v)           
            arr = self.glist[v]
            for elem in arr:
                print("elem:" , elem)
                if elem not in check_list:
                    if elem not in Q.queue:                 
                        Q.enqueue(elem)
                        print("Queue:", Q.queue)
            
        return check_list
    def DFT(self, start_node):
        myglist = self.glist
        s = myStack()
        outlist = []
        outlist.append(start_node)
        s.push(start_node)
        arr = myglist[start_node]
        while(len(s) != 0): 
            n = s.pop()  
            arr = myglist[n]  
            if (self.isvisited(s.mystackl,arr)) == 1:
                taken = s.pop()
            else:
                for elem in arr:
                    if elem not in s.mystackl:
                        if elem not in outlist:
                            s.push(elem)
                            outlist.append(elem)


        return outlist
        
list_nodes= [1,2,3,4,5]
dictpass ={}
graphDict = {}
g1 = graphs()
mgraph = [{1:[2,3]} , {2:[1,3,4]} , {3:[1,2,5]} ,{4:[2,5]} , {5:[4,3]}]
for nodes in mgraph:
    print(nodes)
    g1.addVertex(nodes)
g1.addVertex({1:[2,3]})
arr = g1.BFT(3)
print(arr)
arr = g1.DFT(2)
print(arr)

