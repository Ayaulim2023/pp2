n = int(input())
m = int(input())
k = int(input())
z = 0
if(n==m==k):
    z=3
elif(n==m):
    z+=2
elif(n==k):
    z+=2
elif(m==k):
    z+=2
print(z)
