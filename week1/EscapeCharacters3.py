txt = 'It\'s alright.'
print(txt) 

txt1 = "This will insert one \\ (backslash)."
print(txt1)

txt2 = "Hello\nWorld!"
print(txt2) 

txt3 = "Hello\rWorld!"
print(txt3)

txt4 = "Hello\tWorld!"
print(txt4)

#This example erases one character (backspace):
txt5 = "Hello \bWorld!"
print(txt5) 

#A backslash followed by three integers will result in a octal value:
txt6  = "\110\145\154\154\157"
print(txt6) 

#A backslash followed by an 'x' and a hex number represents a hex value:
txt7 = "\x48\x65\x6c\x6c\x6f"
print(txt7) 


