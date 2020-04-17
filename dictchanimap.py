import collections #for creating alternative containers to already existing data types in
#python like dict, tuples, list, set
import re


cnt = collections.Counter() #creates a hashable list with each key tied to their number
#of occurences
lst = ['a' , 'b', 'a' , 'b' , 'c'] 
for k in lst:
    cnt[k]+=1
print(cnt)
mset = set()
mset.add('amulya' )
print(mset)
w = []
w +=mset

Days=set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun" , "Mon"])
Months={"Jan","Feb","Mar"}
Dates={21,22,17}
w += Days
print(w)
print(Days)
print(Months)

print(Dates)
dict1 = {'a': 10, 'b': 20 , 'c': 30 }
dict2 = {'d' : 40, 'e':50 , 'f': 60 }
adele = set(["hallo", "from" , "the", "other", "side"])
print(adele)
print(["hallo", "from" , "the", "other", "side"])
#dict3 = collections.ChainMap(dict1 , dict2)

s
