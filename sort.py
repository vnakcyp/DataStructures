def find_length(lst):
    print("iam in find_length")
    return len(lst)
def ifindmax(lst):
    print("i find max")
    a = 1
    for i in range(find_length(lst)):
        if(a<lst[i]):
            a = lst[i] 
        else :
            continue
    return a

def iamsort(lst):
    print(lst)
    for i in range(len(lst)-1):
        for j in range(len(lst)-i-1):
            if(lst[j] > lst[j+1]):
                lst[j] , lst[j+1] = lst[j+1] , lst[j]
    return lst


lst = [2,3,5,1]
lst = [5,4,3,2,1]

print(len(lst))
for i in lst:
    print(i)
for a in range(len(lst)):
    print(a)
lst.append(12)
print(find_length(lst))
print(ifindmax(lst))
print(iamsort(lst))
