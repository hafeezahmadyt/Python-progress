#boolean
a = 200
b = 300
c=0
if b > a:
    print("B is greater")
else:
    print("a is greater")

print(bool(c))    #will return false bcs zero

def boolfunction(): #Function That return bool
    return True
print (boolfunction())

if boolfunction():
    print("Is returning true")
else:
    print("Returing False")    

#isinstance func is used to check data type

print(isinstance(a,str))    
print(10>9)

#operators 
if a==b :
  print('a is equal to b')
else:
    print('Is not equal')  

c= 4020
d=200
print(c/d)    
print(c//d)   #floor division will round off answer
print(a*b)
print(a**b) #it finds exponention like it will multiply a*a*a.. b times
print (a>=0 and b == 0) #will return false bcs B is not equal to zero 
print (not(a>=0 and b == 0)) #NOT reverse the results 

#membership operator
fruits = ['apple','orange','strawberry']
print('apple' in fruits)

if 'orange' in fruits:
  print('availavle')
else:
  print('not Available')

print(3<<3) #will add 3 zeros to its binary 3=0011 11000=24
print(~3) #it inverts all bits  3 = 0000000000000011
#-4 = 1111111111111100

print(20>>3)

print((20+10)+(30+90)) #inside paranthesis will add first
print(100+200*1) #BODMAS rule
print(10+23-23+10) #As + and -  has same precednce therefor it will work from left to right

#list 
myFirstList = ['data1','data2','data3']
print(myFirstList)
print(type(myFirstList))