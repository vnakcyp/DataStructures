mydict = {2:[] , 3:[] , 5:[] }
def hashfunc(val):
    myList = [2,3,5]
    for i in myList:
        if((val % i ) == 0):
            mydict[i].append(val)
            break
global accum 
accum = 0
def fibo(n):
    if n <= 1:
        global accum+=1
        return n
    else:
        accum+=1
        return (fibo(n-1) + fibo(n-2))

nterm = 11
if nterm <= 0:
    print("enter positive")
else:
    print("Fibonacci")
    for i in range(nterm):
        print(fibo(i))
        hashfunc(fibo(i))
print(mydict)



myhashtable = {'vegetable':[1,3], 'fruits': [2,3], 'meat':[3,3]}
print(myhashtable['vegetable'])
from collections import defaultdict
data = [(2010, 2), (2009, 4), (1989, 8), (2009, 7)]
mydict = defaultdict(list)
#val = []
#mydict = defaultdict(lambda : val)
print(mydict)
for year,month in data:
    mydict[year].append(month)

print(mydict)
#print(mydict)
