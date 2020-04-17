#find the medians for the individal sorted arrays, compare with each other,
#find subarrays from the medians
def iamsort(lst):
    print(lst)
    for i in range(len(lst)-1):
        for j in range(len(lst)-i-1):
            if(lst[j] > lst[j+1]):
                lst[j] , lst[j+1] = lst[j+1] , lst[j]
    return lst
def midfind(a):
    return ((a+1)/2  if a%2 == 1 else a/2)
def medianed(lst1 , lst2):
    itr = 0
    a = len(lst1)
    b = len(lst2)
    itr = a if a <= b else b
    mid1 = midfind(a)
    mid2 = midfind(b)
    for i in range (itr/2):
        if (lst1[mid1] < lst2[mid2]):
            lst1 = lst1[mid1:]
            lst2 = lst2[:mid2]
        else :
            lst1 = lst1[:mid1]
            lst2 = lst2[mid2:]
    comlst = []

    comlst.append(lst1[0] if lst1[0] > lst2[0] else lst2[0])
    comlst.append(lst1[1] if lst1[1] < lst2[1] else lst2[1])
    return ((comlst[0] + comlst[1])/ 2)


lst1 = [3,1,4,6,2]
lst1 = iamsort(lst1)
lst2 = [4,2,7,5,8]
lst2 = iamsort(lst2)
v = medianed(lst1 , lst2)

print(v)

