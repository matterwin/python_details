ex1 = 'This is a string'
ex2 = "This is also a string"           # can use ' in "" w/o using espace chars
ex3 = ""

ex4 = "0123456"         # strings are accessed by index numbers like char arrays in Java or strings in C/C++

ex5 = "orange"
print(ex5[2])               # prints a
print("apple"[4])           # prints e

# string slicing i.e. substrings in a way but in python ez
ex6 = "apricots"

print(ex6[:3])              # apr
print(ex6[2:5])             # ric
print(ex6[4:])              # cots

# concatenation
print("pecan" + " " + "pie")       # pecan pie

concatenated = "R2" + "-" + "D2"
print(concatenated)                 # R2-D@
print(concatenated[3])              # D
print(concatenated[1:4])            # 2-D

# silicing doesn't effect the string unless you actually reassign that var to its sliced version

to_slice = "Just do it!"
print(to_slice[10])   # prints "!"
print(to_slice[5:7])  # prints "do"
print(to_slice[8:])   # prints "it!"
print(to_slice[:4])   # prints "Just"
print("Don't " + to_slice[5:])  # prints "Don't do it!"

# types

ex1 = False
ex2 = 29
ex3 = 4.1352

print(type(ex1))    # <class 'bool'>
print(type(ex2))    # <class 'int'>
print(type(ex3))    # <class 'float'>

# string conversion

ex4 = str(3.21)
print(type(ex4))     # <class 'str'>

# escape sequences

# \t    tab character
print("This\tis\ta\tlot\tof\tspace.")           #This    is    a    lot    of    space

# /n    newline character
print("line one\nline two")                     # line one
                                                # line two

# \' and \""
#just adding ' or " to a string

# \\
# just adds \ to a string

float_num = 6.7                                     # variable that has been assigned a float
print(type(float_num))                              # prints the type of float_num
print(str(float_num) + " is a float.")              # prints "6.7 is a float."
print("\"Hello, I'm Aaron, it's nice to meet you!\"")  # prints "Hello, I'm Aaron, it's nice to meet you!"

print("*******\n *****\n  ***\n   *")

# input function

name = input("Please enter your name.")
print("Your name is " + name + ".")
print(type(name))       # <class 'str'>

name = input("What is your name?")
quest = input("What is your quest?")
color = input("What is your favorite color?")
 
print("So your name is " + name + ", your quest is " + quest + ", and your favorite color is " + color + ".")

# integer input method
userInt = int(input("Please enter an int"))
print(userInt)
print(type(userInt))      # <class 'int'>

# float method
userFloat = float(input("Please enter an int"))
print(userInt)
print(type(userInt))      # <class 'float'>