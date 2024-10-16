#tuple
Tuple = ('apple','kiwi','banana','mango')
print(Tuple)
#tuples are unchangable means we cannot add or remove anything after they are created
print(len(Tuple))

#create tuple with one item we use , in end
myTuple =('hafeez',)
print(myTuple)

#Below is not tuple
myTuple =('hafeez')
print(myTuple)

#Tuple can hold multiple data types
MyTuple = ('hafeez','aziz',12,12,32,False,True,2,4)
print(MyTuple)

result = MyTuple[2] +  MyTuple[3]
print(result)
print(MyTuple[2])
print(MyTuple[2] +  MyTuple[3])
print(type(MyTuple))

#create  constructor of Tuple class to make Tuple
newTuple= tuple(('hello','123',132))

#negative Index Means start from End

print(MyTuple[-2:])
print(MyTuple[:5])
print(MyTuple[-2:-1])
#lets check if available in tuple

if 'hafee' in MyTuple:
    print('Yes Exist')
else :
    print('Not Available')    

#with below code you can update tuple by converting it into list
names = ('hafeez','anees','ahmad')
enames = list(names)
print(enames)
enames[1]='hussain'
names = tuple(enames)
print(names)

#Now lets add items to it
anames = list(names)
anames.append('zain') #you can add only one name
names = tuple(anames)
print(names)
 
#lets rewrite for practice
numbers = (1,2,3,4,5) #we have to add 6 and 7 in it
x = list(numbers)
x.append(6)
x.append(7)
numbers = tuple(x)
print(numbers)

#Removing items from tuple
num = (1,2,3,4,5)
x = list(num)
x.pop(0)
num = tuple(x)
print(num)

#completely deleting Tuple
del num

#ok so lets  talk about packing and unpacking
num = (1,2,3,4,5) #Packing
(item1,item2,*item3)=num #unpacking
#by using Sterik the remaining item will be added to it 
print(item3)

#Loop through tuple
Tuple = ('apple','kiwi','banana','mango')
for x in Tuple:
    print(x)

#using index number
for x in range(len(Tuple)):
    print(Tuple[x])

#Using while loop to iterate through tuple
i = 0
while i < len(Tuple):
    print(Tuple[i])
    i= i+1

#joining tuples 
newTuple = numbers + Tuple
print(newTuple)

#Multiplying a tuple
newt = numbers * 3
print(newt.count(1)) #It will count how many 1 are in the tuple

#Set

MySet = {'apple','banana','orange','Mango'}
print(MySet)
#Set items are unordered every time you print them will have different values

#set items should not be duplicated
#The values True and 1 are considered the same value in sets, and are treated as duplicates
print(len(MySet))

#set can also hold multiple data types
myNewSet = {'Name','city',12,12,43,1,True,0}
print(myNewSet)

newset = set(('1,2,3,4'))
print(newset)

#loop through set

for x in newset:
    print(newset)

print('Name' in myNewSet) #chechk if available in set or not

#once set is created you cannot change items but you can add and remove items
#adding items

myNewSet.add("oranga")
print(myNewSet)

#update is used to add items from one set to other
newset.update(myNewSet)
print(newset)

#with update function you can add dictionaries,tuples and list to it

