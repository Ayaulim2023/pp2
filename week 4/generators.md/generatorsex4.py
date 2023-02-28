def squares(a,b):
    for i in range(a,b):
        yield i**2
        i+=1


a = int(input())
b = int(input())
for i in squares(a,b):
  print(i)
