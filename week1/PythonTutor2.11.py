n = int(input())
m = int(input())
x = int(input())
y = int(input())

if m<n:
    if m-x<x:
        x=m-x
    if n-y<y:
        y=n-y
else:
    if n-x<x:
        x=n-x
    if m-y<y:
        y=m-y

if x<y:
    print(x)
else:
    print(y)