max = 0
m1 = -1
e = -1
l = 0
while e != 0:
    e = int(input())
    if e > max:
        max = e
        m = l
    l += 1
print(m)