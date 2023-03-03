#first
import re

txt = "The rain in Spain"

#Check if the string starts with "The":

x = re.findall("\AThe", txt)

print(x)

if x:
  print("Yes, there is a match!")
else:
  print("No match")

#second
x1 = re.findall(r"\bain", txt)

print(x1)

if x1:
  print("Yes, there is at least one match!")
else:
  print("No match")

#third
x2 = re.findall(r"ain\b", txt)

print(x2)

if x2:
  print("Yes, there is at least one match!")
else:
  print("No match")

#fourth
x3 = re.findall(r"\Bain", txt)

print(x3)

if x3:
  print("Yes, there is at least one match!")
else:
  print("No match")

#fifth
x4 = re.findall(r"ain\B", txt)

print(x4)

if x4:
  print("Yes, there is at least one match!")
else:
  print("No match")

#sixth

#Check if the string contains any digits (numbers from 0-9):

x5 = re.findall("\d", txt)

print(x5)

if x5:
  print("Yes, there is at least one match!")
else:
  print("No match")

#seventh

#Return a match at every no-digit character:

x6 = re.findall("\D", txt)

print(x6)

if x6:
  print("Yes, there is at least one match!")
else:
  print("No match")


#eighth

#Return a match at every white-space character:

x7 = re.findall("\s", txt)

print(x7)

if x7:
  print("Yes, there is at least one match!")
else:
  print("No match")


#nine

#Return a match at every NON white-space character:

x8 = re.findall("\S", txt)

print(x8)

if x8:
  print("Yes, there is at least one match!")
else:
  print("No match")

#ten

#Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character):

x9 = re.findall("\w", txt)

print(x9)

if x9:
  print("Yes, there is at least one match!")
else:
  print("No match")

#eleven

#Return a match at every NON word character (characters NOT between a and Z. Like "!", "?" white-space etc.):

x10 = re.findall("\W", txt)

print(x10)

if x10:
  print("Yes, there is at least one match!")
else:
  print("No match")

#twelve

#Check if the string ends with "Spain":

x11 = re.findall("Spain\Z", txt)

print(x11)

if x11:
  print("Yes, there is a match!")
else:
  print("No match")

