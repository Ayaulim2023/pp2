n = int(input())

def squares(a,b):
    while a<=b:
        yield a*a
        a+=1
 
for i in squares(1,n):
    print(i)