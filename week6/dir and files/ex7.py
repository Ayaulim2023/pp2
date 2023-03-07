with open(r'C:\Users\ASER\Desktop\pp2\week6\dir and files\example.txt','r') as firstfile, open(r'C:\Users\ASER\Desktop\pp2\week6\dir and files\example2.txt','a') as secondfile:
      
    # read content from first file
    for line in firstfile:
               
             # append content to second file
             secondfile.write(line)