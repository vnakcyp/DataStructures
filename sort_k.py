import heapq as hq
from heapq import heapify

# def heapSort(arr):
#     l = len(arr)
#     for i in range(l):
#         arr[0] , arr[l-1] = arr[l-1] , arr[0]
#         heapify(arr)
#     return arr





arr = [2,3,4,5,4,1,8]
heapify(arr)
print(arr)
# arr[0] , arr[len(arr) -1] = arr[len(arr)-1] , arr[0]
l = len(arr)
# hq.heappush(arr , 10)
# for i in range(l):
#     arr[0] , arr[l-i-1] = arr[l-i-1] , arr[0]
#     print(arr)
#     heapify(list(arr[0:l-i-1]))
# print(arr)
# for i in range(l):
    
#     print(i)
#     k = (arr[i:l-1])
#     print(k)
#     heapify(k)
#     print(k)
#     arr[i:l-1] = k
#     print(arr)
# print(arr)
for i in range(l):
    
    k = (arr[i:l-1])
    heapify(k)
    arr[i:l-1] = k
print(arr)

# h = []
# for value in arr:
#     hq.heappush(h , value )

# print(h)
# arr = heapSort(arr)
# print(arr)
# print([x for x in range(10 ,0)])


