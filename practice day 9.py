#copy one  Dictionery to Other
Dictcar = {'brand' : 'Suzuki','year':'2008','model':'Bolan'}
newdict = Dictcar.copy()
print(newdict)

#We can use Dict() function for the same task

newdict1 =dict(Dictcar)
print(newdict1)

#Nested Dictioneries (Dict in Dict)
myFamily = {
    'child1':{
        'name':'Ahmad',
        'year':'2020'
    },
    'child2':{'name':'Umer','year':'2021'},
    'child3':{'name':'ali','year':'2019'}

}

#accessing nested Dictionaries
print(myFamily['child1']['name'])

#now accesing through loop 
for c,obj in myFamily.items():
    print(c)

    for y in obj:
        print(y + ':',obj[y])

for y in myFamily.items():
    print(y)

# if else statement and also elif
a = 30
b = 30
if b > a:
    print('b is greater than a')
elif a > b:
    print('a is greater than b')

else:
    print('a is equal  b') 

#short hand if 
if a == b : print("hello")
#if else statement
print("A") if a>b else print("b")

#with three conditions
print('A') if a>b else print('B') if a==b else print('c')

#And statement
if a>b and b<a:
    print('yes a is bigger')

#Not statement 
if not a > b:
    print('a is not greater')

#Nested if
x = 31
if x > 10:
    print('Above ten')
    if x > 20:
        print('and also above 20')
    else:
        print('but not above 20.')

#pass statement
if b < a: # having an empty if statement like this, would raise an error without the pass statement

    pass