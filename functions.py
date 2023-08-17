def function_name():
    print(2 + 2)


function_name()         # prints 4
#functions should have 2 lines of space above and below it for best practice styling


def function_name2(parameter):
    print(parameter + 2)


function_name2(8)        # prints 10
first_str = "The number "


def function_name(p1, p2, p3): #can reassign function names & here are the parameters
    print(p1 + str(p2) + p3)


function_name(first_str, 5, " is an integer.") #here are the arguments

# can give default values to parameters


def default_example(num1=7, num2=8):
    print(num1 * num2)


default_example() # 56
default_example(2) # 16
default_example(2, 3) # 6

# return keyword


def default_example(num1=7, num2=8):
    return (num1 * num2)


print(default_example()) # 56


def name_printer(user_name):
    print(user_name)
 
 
name = input("Please enter your name.")
name_printer(name)

length = int(input("Enter an integer that represents length in feet."))
width = int(input("Enter an integer that represents width in feet."))
height = int(input("Enter an integer that represents height in feet."))
 
 
def prism_vol(l, w, h):
    return l * w * h
 
 
print("The volume of the rectangular prism is " + str(prism_vol(length, width, height)) + " cubic feet.")


celsius = int(input("Please enter an integer value for degrees celsius. "))
 
 
def fahrenheit(cel):
    # To avoid the approximation error that would occur if the float 1.8 was used in the calculation, 1.8 * 10 is used
    # instead, resulting in the integer 18.  To balance this out, 32 is also multiplied by 10 to get 320.  After the
    # calculations in the parentheses are finished, the result is divided by 10, which gives the correct Fahrenheit
    # temperature.
    return (18 * cel + 320) / 10
 
 
print("The Fahrenheit equivalent of " + str(celsius) + " degrees Celsius is " + str(fahrenheit(celsius)) + ".")


