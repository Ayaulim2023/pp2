n = int(input())
m = 2
k= 1
while m <= n:
    m *= 2
    k += 1
print(k - 1, m // 2)