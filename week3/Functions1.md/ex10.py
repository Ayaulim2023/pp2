def unique_elements(list):
    new_list=[]
    for i in range(len(list)):
        if list[i] not in new_list:
            new_list.append(list[i])
    return new_list

list = []
n = int(input())
for i in range(n):  
    new_element = int(input())  
    list.append(new_element) 
print(unique_elements(list))