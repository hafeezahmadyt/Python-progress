#String are arrays
name = 'hafeez ahmad'
print(name[2])
print(name[1])

#loop in string
for x in "hafeez":
 print(x)

for x in name:
 print(x)

 #length of string
print(len(name))
print(len(x))

#check string
txt = 'hello this is hafeez ahmad'
print('hafeez ahmad' in txt)

if 'hello' in txt:
 print('yes present')
if 'hello' not in txt:
 print('not available')

#slicing
print(name[2:8]) #will start from 2 end on 8
print(name[:8]) #will start from 0
print(name[3:]) #will print till end

print(name)
name1 = 'hello'  

#Upper and Lower
print(name.upper())
print(name.lower())

#More Methods with string
print(name.strip()) #Removes spaces Str and End
print(name.replace('hafeez','m'))
print(name.split("a")) #splits the string where "a" is located

#string merging
txt1 = "hello"
txt2 = "how are you"
full_txt = txt1+" "+txt2
print(full_txt)

#string format and F string
amount = 20000
#txt = "my salary is " + amount will not work

txt = f"my salary is {amount:.3f}" #3f means 3 decimal points
print(txt)
txt =f"the sum is {20+20}"