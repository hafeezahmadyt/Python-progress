carlist =['suzuki','toyota','mercedes']
carlist.remove('toyota')
print(carlist)



#for loop

for x in carlist:
    print(x)

listofname = ['hafeez','aziz','ahsan','akeel','nawaz']
for n in  range(len(listofname)):
  print(listofname[n])  


  #for h in range(10):
   # print(h)


thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
 print(thislist[i])
 i += 1 

 #for loop short form
 [print(h) for h in  carlist]


#using for loop to create new list on basis of existing

fruits = ['apple','banana','orange','kiwi','mango','pineapple']
fruit = []
for x in fruits:
  if 'i' in x:
    fruit.append(x)

print(fruit)

#list comprehension
fruits1 = ['apple','banana','orange','kiwi','mango','pineapple']

newlist1 = [x for x in fruits1 if 'pp' in x]
newlist2=[i for i in fruits1 if 'ap' in i]
print(newlist1,newlist2)

Noapplelist = [x for x in fruits if x != 'apple']
print(Noapplelist)

#the  above if condition is optional and new list can be created without it
newlist1 =[x.upper() for x in fruits]
print(newlist1)


#iteratble
iteratelist = [x for x in range(10)]
# iteratelist = [x for x in range(10) if x < 4] 
print(iteratelist)

#replace part in list
newlist3 = [x if x == "apple" else 'fruit ' for x in fruits]

print(newlist3)