#age =[int(input("Enter Age : "))for x in range(3)]

#age.sort(reverse=True)
#print('Biggest age is : ', age[0])

#user will input two numbers,Program will swap the numbers

#num1 = input('Enter first number')
#num2 = input('Enter the second number')
#x = num1
#y = num2 
#num1 = y
#num2 = x

#print(num1,num2) #it will swap the numbers

#write a program that will give u sum of 3 digits
#num1 = input('Enter first number')
#num2 = input('Enter the second number')
#num3 = input('Enter third Number')
#sum = int(num1) + int(num2) + int(num3)
#print('Sum of three numbers :',sum)

#write a program that Number puted is odd or even
#num = input('Enter the number : ')

#num =[int(input("Enter num : "))for x in range(3)]
#num.reverse()
#print(num)

#User will input cost and selling price and will say if loss or profit
cost = input('Enter cost : ')
sell = input('Enter Selling rate : ')
if cost>sell:
    acc = int(sell) - int(cost)
    print(f'You  loss {acc}')
else:
    acc = int(sell) - int(cost)
    print(f'You  profited {acc}')