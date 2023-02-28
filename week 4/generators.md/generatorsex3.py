def EvenGenerator(n):
    i=0
    while i<=n:
        if i%3==0 and i%4==0:
            yield i
        i+=1


n=int(input())
values = []

for i in EvenGenerator(n):
    values.append(str(i))
i_iter = iter(values)
for i in EvenGenerator(n):
  print (next(i_iter))