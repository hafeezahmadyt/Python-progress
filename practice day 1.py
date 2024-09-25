#Storing multiple values to multiple variables
a,b,c,d = 12,23,32,"hafeez"
print(a,b,c,d,)
print(d)
print(d,a,c)

#one value to multiple variables
a=b=c=d=23
print(a,b,c,d)

#conept of unpacking

cars = ['bentley','suzuki','toyota']
car1,car2,car3= cars
print(car1)
print(car2)
print(car3)

#using + operator
print(car1+car2+car3)
print("hello this car name is "+car2)

#global vs local variable 
x = 'hi' #Global variable out of Scope

def myfunc():
    #global x used to convert local to global
    x = 'bye' #Local variable Inscope
    print("i am saying "+x)
myfunc()

print('i am saying '+x)

x = (1+2j)
print(x)
print(type(x))

#Random Number
import random
print(random.randrange(1,50))

#multi line strings
a = """hello
how you doing
welcome
"""
print(a)