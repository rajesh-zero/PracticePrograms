#variable and datatype

x=1
y='ddfsdfs'
b=['hi','hello','how']
c=('hi','hello','how')
print(type(x))
print(type(y))
print(type(b))
print(type(c))

#type casting
x='5'
y=5
#print(x+y) gives error
print(str(y)+x)
print(int(x)+y)

a,b='4','5'
print(a+b)
print(int(a+b)+4)


i=input("enter something")
print(i)