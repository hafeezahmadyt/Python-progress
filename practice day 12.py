#In python theres no Arrays we can use list as arrays
cars = ['Ford','Bolan','BMW']
x = cars[0]
print(x)

#Modifying value of first array

cars[0]='Mustang'
print(cars)

print(len(cars)) #Return Elements of array

#looping through arrays
for x in cars:
 print(x)

 #Pop() Method is used for removing items from the list with providing index number
 cars.pop(1)
 #Also we can use Remove() Method to remove items by providing item name
 cars.remove('BMW')
 print(cars)

#Classes and Objects
class MyClass:
 x = 5

#lets create object of it
p1 = MyClass()
print(p1.x)


class person:
 def __init__(self,name,age):
  self.name =  name
  self.age  = age
  
p1 = person('john',34)

print(p1.name,p1.age)
print(p1)



