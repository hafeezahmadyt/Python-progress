#append
list = ['apple','banana','orange','mango']
print(list)
list.append('kiwi') #will add item at the end of list
print(list)

#Extent
list2 = ['green','yellow','white']
list.extend(list2) #it will add elements from 2nd to 1st list
print(list)

#Extent can work btw tuples,sets,dictionaries etc
MyTuple =('ali','Hamza','hafeez')
list2.extend(MyTuple)
print(list2)

list.remove('orange') #if theres 2 on same name then first will be removed
print(list)
#remove

#pop
print(list)
list.pop(2)
print(list)
#simple pop() will remove the last item
list.pop()
print(list)

#Del
#it works as pop() but empty del can delete entire  list
del list[0]
print(list)
#del list #will delete entire list
print(list)

list.reverse()
print(list)