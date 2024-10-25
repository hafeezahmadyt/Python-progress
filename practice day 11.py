#nested for loop
colors = ['red','green','blue']
fruits = ['Apple','Banana','Pineapple']

for x in colors:
    for y in fruits:
        print(x,y)

#for loops can not be empty but still if you want to run empty for loop you can use pass statement not to get error

for x in [0,1,2]:
    pass

#Iterators
myTuple = ('apple','Banana','kiwi')
myIt = iter(myTuple)
print(next(myIt))
print(next(myIt))
print(next(myIt))

#we can use iterators on strings too
name = 'Hafeez'
myit = iter(name)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

#functions
#Function is defined using def keyword
def MyFunction():
    print("I am called")

MyFunction() #calling function

#Function with arguments
def Myname(name):
    print('My name is ',name)

Myname('Hafeez')
Myname('Ihtisham')

#function with two arguments
def Yournames(Cname,Fname):
    print(f"My name is {Cname} and my father name is {Fname} ") 

Yournames('Hafeez','Shabir')

#If the number of Arguments is Unknown we can add * before arguments
def Childrens(*kids):
    print("Youngest Child is ",kids[0])

Childrens('Umer','Junaid','ali')

#using Dictoinary in functions
def passDict(child3,child2,child1):
    print('The youngest child is ' + child3)

passDict(child1='Aziz',child2='Shakeel',child3='Hafeez')    

#if the number of keywords is unknown we can use double sterik ** before the parameter
def Func(**kid):
    print('Name of child is '+ kid['kname'])

Func(fname = 'Aziz',kname='umer')

#default vallue in funtion 
def myFunction(Country = 'Norway'):
    print('I am from ',Country)

myFunction("pakistan")
myFunction() #will call default parameter

#passing a list as an Argument
def my_Function(food):
    for x in food:
        print(x)

fastfood  = ['Burger','Pizza','fries']
my_Function(fastfood)       

#lets use return value
def mulfive(x):
    return 5 * x
print(mulfive(10))

#if your function is empty you can use pass statement to save from error

def myfunction():
  pass

#In keyword only Arguments we cant pass argumnnets directly but we have to use names to pass values
def newFunc(*,Model,year):
    print(f'The model of car is {Model} and is made in {year}')

newFunc(Model='civic',year=2020)

#lambda function
x = lambda a,b,c : a + b + c
print(x(1,2,3))