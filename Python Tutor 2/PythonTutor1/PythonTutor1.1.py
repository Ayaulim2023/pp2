a = int(input())
b = int(input())
if(a<b):
    for x in range (a,b+1):
        print(x,end=' ')
elif(a>b):
    for y in range(a,b-1,-1):
        print(y,end=' ')
 