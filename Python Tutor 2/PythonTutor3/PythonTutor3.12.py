m = 0
m2 = 0
e = -1
while e != 0:
    e = int(input())
    if e > m:
        m, m1 = e, 1
    elif e == m:
        m1 += 1        
print(m1)
