x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

z = 0

if x1==x2 or y1==y2:
    z+=1

if abs(x1-x2)==abs(y1-y2):
    z+=1

if z>=1:
    print("YES")
else:
    print("NO")