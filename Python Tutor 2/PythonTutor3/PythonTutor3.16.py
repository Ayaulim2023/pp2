x = int(input())
n = []
while x != 0:
    n.append(x)
    x = int(input())
    
M = sum(n)/len(n)
STD = 0
for i in n:
    STD += (i-M)**2
STD = ( STD/(len(n)-1) )**0.5
print(STD)