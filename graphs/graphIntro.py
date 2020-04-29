import random as r
ARR = [1,2,3,4,5]


class graphs:    
    glist = {}
    def __init__(self, glist=None):
        self.glist = glist  
    def keyChecker(self, key):
        for vrtx in self.glist:
           # print(type(vrtx))
            if( vrtx == key[0]):
                print("alredy pressent")
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
                    edgecol.append({nvrtx , vrtx}) # use sets to represent edges since the order doesn't matter in sets.
                    
                
        




list_nodes= [1,2,3,4,5]
dictpass ={}
graphDict = {}

for i in range(1,6):
    arr = list_nodes[:] # or use copy.deepcopy
    left = r.choice(arr)
    rite = r.choice(arr)
    if(left == rite):
        graphDict.update({i : left})
    else:
        graphDict.update({i : [left , rite]})
    
    print(graphDict)
    print(arr)
g = graphs(graphDict)
dictadd = {5:[1,3]}
#print(int(dictadd.keys()))
g.addVertex({5:[1,3]})


  

   

