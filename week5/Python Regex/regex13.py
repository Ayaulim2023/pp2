#1
import re

txt = "The rain in Spain"

#Check if the string has any a, r, or n characters:

x = re.findall("[arn]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

#2
#Check if the string has any characters between a and n:

x1 = re.findall("[a-n]", txt)

print(x1)

if x1:
  print("Yes, there is at least one match!")
else:
  print("No match")

#3
#Check if the string has other characters than a, r, or n:

x2 = re.findall("[^arn]", txt)

print(x2)

if x2:
  print("Yes, there is at least one match!")
else:
  print("No match")

#4

#Check if the string has any 0, 1, 2, or 3 digits:

x3 = re.findall("[0123]", txt)

print(x3)

if x3:
  print("Yes, there is at least one match!")
else:
  print("No match")

#5

txt2 = "8 times before 11:45 AM"

#Check if the string has any digits:

x4 = re.findall("[0-9]", txt2)

print(x4)

if x4:
  print("Yes, there is at least one match!")
else:
  print("No match")

#6

#Check if the string has any two-digit numbers, from 00 to 59:

x5 = re.findall("[0-5][0-9]", txt2)

print(x5)

if x5:
  print("Yes, there is at least one match!")
else:
  print("No match")


#7

txt = "8 times before 11:45 AM"

#Check if the string has any characters from a to z lower case, and A to Z upper case:

x6 = re.findall("[a-zA-Z]", txt2)

print(x6)

if x6:
  print("Yes, there is at least one match!")
else:
  print("No match")


#8
#Check if the string has any + characters:

x7 = re.findall("[+]", txt2)

print(x7)

if x7:
  print("Yes, there is at least one match!")
else:
  print("No match")