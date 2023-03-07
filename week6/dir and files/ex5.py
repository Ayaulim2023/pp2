l = ['a','b','c','d']

with open(r"C:\Users\ASER\Desktop\pp2\week6\dir and files\example.txt","w") as file:
    for items in l:
        file.write('%s\n' %items)


file.close()