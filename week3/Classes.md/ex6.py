list = []
n = int(input())
for i in range(n):  
    new_element = int(input())  
    list.append(new_element) 


for i in range(n):
    list = filter(lambda x: x == i or x % i, list)
print(list)