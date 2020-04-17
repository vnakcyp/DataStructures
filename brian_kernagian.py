import sort
def FindOnesInteger(a):
    count = 0
    while a :
        a = a & (a-1)
        count=count+1
    return count

def iamsort(lst):
    print(lst)
    for i in range(len(lst)-1):
        for j in range(len(lst)-i-1):
            if(lst[j] > lst[j+1]):
                lst[j] , lst[j+1] = lst[j+1] , lst[j]
    return lst

lst1 = [3,2,4]
lst2 = [4,1,3,7,8]
lst3 = iamsort(lst1+lst2)
lst1 = iamsort(lst1)
lst2 = iamsort(lst2)

print(lst3)


print(FindOnesInteger(10))

