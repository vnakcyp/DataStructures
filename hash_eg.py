dict = {'a' : 2 , 'b':3 , 'c':5}
print(dict['a'])

def factorial(n):
    if( n  <= 1 ):
        return 1
    else :
        return n*factorial(n-1)

def printStar(n, orient):    
    if(n < 1):
        return
    else:
        if(orient ==1):
            printStar(n-1, 0)
        for i in range(n):
            print('*'),  
        print('')   
        if(orient == 0):
            printStar(n-1, 1)             
        return
print(factorial(4))
printStar(5,0)
