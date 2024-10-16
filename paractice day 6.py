newlist = ['0range','mango','peach','banana']
# newlist.sort() #it sorts alphabaticaly
numbers=[1,2,3,3,7,2,3,6,7,1]
# numbers.sort() #it will sort numericaly
# print(newlist,numbers)
# numbers.sort(reverse=True) #it will sort in decending order
# print(numbers)

# def myf(n):
#     return abs(n*2)

# numbers.sort(key=myf)
# print(numbers)

# #ok so the sort() func is case sensitive it sort capital letters first

# #solution
# newlist.sort(key=str.lower)
# print(newlist)

#newlist= list(numbers) #copy() is used to transef data from list to other it will over write the existing data
#we can also use List() which do same as copy()

print(newlist)

#joining lists
list1 = [1,2,3,4]
list2 =[5,6,7,8]
#list3 =list1+list2
#print(list3)

#append
for x in numbers:
    newlist.append(x)

print(newlist)


