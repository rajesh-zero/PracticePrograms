#guess exercise
y=16
print("enter no \n")
while(True):
    x=int(input())
    if x==y:
        print("got me")
        break
    elif x>y:
        print("enter lesser number")
    else :
        print("add greater no")