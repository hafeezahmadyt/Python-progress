#while loop
i = 1
print('hello')
while i < 1000:
    print(f'Number : {i} ')
    i += 1
    if i == 100:
        break #it will break the statement 

#continue
i=1
while i < 100:
    print(i)
    i = i+1
    if i == 50:
        continue
    print('-',i)
   
#else statement
while i < 7:
    print(i)
    i = i + 1
else:
    print('i is no longer than 7')   

#for loop
for x in 'banana':
    print(x)    

#we can use continue statement in for loop too
    
fruits = ["apple", "banana", "cherry"] 
for x in fruits:
     print(x)   
     if x == 'banana':
        break

#now continue statement
cars = ['ferrari','buggati','tesla']
  
for x in cars:
    if x=='buggati': 
        continue #The continue statement will skip the itteration with buggati and will  continue
    print(x)

#Range() Function
for x in range(5):
    print(x)

for x in range(1,10):#10 will not be included
 print(x)    

#now with third parameter for range value
for x in range(1,50,2): #the third parameter is incrementer by default is (1)
    print(x)
   
#now lets use else stetment in for loop

for x in range(6):
    print(x)
else:
    print('finished')   

    