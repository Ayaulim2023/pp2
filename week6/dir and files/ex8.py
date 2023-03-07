import os
 
path = r"C:\Users\ASER\Desktop\pp2\week6\dir and files\example2.txt"
 

if os.path.exists(path):
    print ("Path of the file exists")

    print("\nFile name of the path:")
    print(os.path.basename(path))

    print("\nDirectory portion:")
    print(os.path.dirname(path))

os.remove(path)