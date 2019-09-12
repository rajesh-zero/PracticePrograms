# Dictionary is nothing but key value pairs
d1={"prasad":"indian","rajesh":"nepali","vipul":"chutiya"}


x=input("enter key")
try:
    (d1[x])
except Exception as e:
    print(e,"not found")
#print(d1[x])
# print(d1)
# print(d1["rajesh"])

# for key in d1:
#     print(key)
# print("")

# for key,value in d1.items():
#     print(key,value)


