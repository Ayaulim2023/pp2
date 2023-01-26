n = int(input())
m = int(input())
k = int(input())

if(n%2==0 and m%2==0 and k%2==0):
    print(n/2 + m/2 + k/2)
elif(n%2!=0 and m%2==0 and k%2==0):
    print((n+1)/2 + m/2 + k/2)
elif(n%2!=0 and m%2!=0 and k%2==0):
     print((n+1)/2 + (m+1)/2 + k/2)
elif(n%2!=0 and m%2!=0 and k%2!=0):
     print((n+1)/2 + (m+1)/2 + (k+1)/2)
elif(n%2==0 and m%2!=0 and k%2==0):
     print(n/2 + (m+1)/2 + k/2)
elif(n%2==0 and m%2!=0 and k%2!=0):
     print(n/2 + (m+1)/2 + (k+1)/2)
elif(n%2==0 and m%2==0 and k%2==0):
     print(n/2 + m/2 + (k+1)/2)