#first
def my_function():
  print("Hello from a function")

#second
def my_function():
  print("Hello from a function")

my_function()

#third
def my_function(fname, lname):
  print(fname)

#fourth
def my_function(x):
  return x + 5

#fifth
def my_function(*kids):
  print("The youngest child is " + kids[2])

#sixth
def my_function(**kid):
  print("His last name is " + kid["lname"])