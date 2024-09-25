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