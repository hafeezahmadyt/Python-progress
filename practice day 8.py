#Removing items from set
#we have two functions remove() and discard()
myNewSet = {'Name','city',12,12,43,1,True,0}
myNewSet.remove(0)
print(myNewSet)

#discard()
myNewSet.discard('Name')
print(myNewSet)

#Difference between remove() and discard() is that remove() raise error when Item is not in the list while Discard() doesnt raise any error

#pop() we can also use this function to remove items from set but the issue is that it will remove random items from set

myNewSet.pop()
print(myNewSet)

#clear() it will clear the entire set
#myNewSet.clear()
print(myNewSet)

#del() isn used to  delete the entire set


#loops
#for loop in set 
for x in myNewSet:
    print(x)

#just like Update we can use Union() to merge two set
nums = {1,2,3,4}
mergeset = nums.union(myNewSet) #The union set returns a new set in which the both are merged
#with union() we can merge more than two set by adding them with coma i.e nums.union(set1,set2)
print(mergeset)

#we can also use | operator to merge two sets works just like union
set1 = {'a','b','c'}
set2 = {1,2,3}
set3 = {'toyota','suzuki',''}
set4 = set1 | set2

print(set3)

#intersection() this func return a  new set that only contain duplicate items
set1 = {1,2,3,4,5}
set2 = {True,False,5}
set3 = set1.intersection(set2)
print(set3)

set4 =  set1 & set2
print('set4 ',set4)

#intersection_update() it is just like intersection() but doesnt create new set but modify the existing one 

#difference it is invert to intersection it will only return items that  are not present in other set
set1 = {1,2,3,4,5}
set2 = {True,False,5}
set3 = set1.difference(set2)
print(set3) #{2, 3, 4}

#we can use - too which work like difference()
set3 = set2 - set1 
print(set3)

#symmetric_difference() it will make new set in which  will contain elements that are not present in both set
set1 = {1,2,3,4,5}
set2 = {True,False,5}
set3  = set1.symmetric_difference(set2)
print(set3)

#dictionary is data type which store values in ket:value pairs
mydic ={'name':'hafeez','fname':'shabir','village':'kotha'}
print(mydic)
print(mydic['name'])
print(len(mydic))

