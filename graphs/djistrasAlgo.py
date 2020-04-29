import sys

def minUnvisited(visited , AccDist):
    index = 0
    k  = 0
    check = False
    print("in min Unvisteid",visited)
    for i in range(len(visited)):
        if visited[i] == False:
            print(visited[i])
            print("K value", k)
            print(AccDist[i])
            k = AccDist[i]
            break
    print("Ist for loop completed")
    print(AccDist)
    for j in range(len(visited)):
        print("loop two")
        if (visited[j] == False) and (AccDist[j] <k ):
            index = j
            k = AccDist[j]
            print("k",k)
            check = True
    print("seconf for loop comp")
    if check == False:
        return i
    else:
        return index
    
   

def djikstra(dims, start_node, matrix,end_node):
    visited = [False] * dims
    AccDist = [sys.maxsize]* dims
    AccDist[start_node] = 0
    print( sys.maxsize)
    i = start_node
    visited[i] = True
   # lastvisited = start_node
    k = 0
    currMinValue = AccDist[start_node]

    # while(i != end_node):
    while(k < 6):
        
        k+=1
        print("i am in loop", k)
        for j in range(dims):
            print("i", i)
            print("j",j),
            if(matrix[i][j] != 0)  and (visited[j] == False) :
                if(AccDist[j] > (matrix[i][j] + currMinValue)):
                    print("Change index " , j)
                    AccDist[j] = matrix[i][j] + currMinValue 
                    print("visited :" , visited)                    
                    print("AccDist:", AccDist) 
        mn = minUnvisited(visited , AccDist) 
        print("minimum Value at", mn)
        visited[mn] = True
        currMinValue = AccDist[mn]
        i = mn
        print("visited :" , visited)                    
        print("AccDist:", AccDist)  

                    
                    
                    
                                     
                    
    
   





matrix = [[0,2,3,0,0,0],
          [2,0,1,6,0,0],
          [3,1,0,0,5,0],
          [0,6,0,0,3,7],
          [0,0,5,3,0,9],
          [0,0,0,7,9,0]]
djikstra(6,0,matrix,5)