import os

path = r"C:\Users\ASER\Desktop\pp2\week5"
if os.path.exists(path):
    print ("Path of the file exists")

    print("\nFile name of the path:")
    print(os.path.basename(path))

    print("\nDirectory portion:")
    print(os.path.dirname(path))