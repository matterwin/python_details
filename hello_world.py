print("hello world")

# run python via: py [python file path]

# var re/assignment
var1 = 2 #int
var1 = 3
var1 = "hi" # string
var1 = False # booleans are capitalized
var1 = True
var1 = 2.0 # floats

#more examples
integer = 7
float_num = 2.718 
bool_val = False
integer = 10

# comments starts with # obviously

# math ops
addition = 4 + 5            # 9
subtraction = 5 - 2         # 3
division = 7 / 2            # 3.5 
multiplication = 3 * 8      # 24

exponentiation = 4 ** 4     # 256 or 4^4 in regular math
floor_division = 16 // 5    # 3 so floor_div rounds down! (in math ans would be 3.2)
modulo = 7 % 3              # 1 i.e. 7 = (3 * 2) + 1 the 1 is the remainder

# assignment shortcuts
add_assign = 5
add_assign = add_assign + 7
add_assign += 7

# subtraction
sub = 10
sub -= 5                # 5

# multiplication
mult = 10
mult *= 5               # 50

# division
div = 10
div /= 5                # 2.0

# expotentiation
exp = 10
exp **= 2               # 100

# floor division
floor = 10
floor //= 6             # 1

# modulo
mod = 10
mod %= 7                # 3

# precedence (1st to last or top to bottom)
# ()
# **
# %, /, //, *           same lvl of precedence so go from left to right
# +, -                  same lvl of precedence so go from left to right

# example:
# ( 9 - 7 ) * 2 ** 3 + 10 % 6 // -1 * 2 - 1
# 2 * 2 ** 3 + 10 % 6 // -1 * 2 - 1
# 2 * 8 + 10 % 6 // -1 * 2 - 1
# 16 + -8 - 1
# 7

# print() method

var2 = 3.14159
print(var2)             # prints 3.14159

print((4+5) * 3)        # prints 60

int_num = 24601   # int_num is a variable which has been assigned an integer
print(int_num)    # prints the integer assigned to int_num
print(True)       # uses print() to display the Boolean value True
print(1 + 1 + 1)  # prints the result of the expression 1 + 1 + 1

# python has approximation errors since its built on C
ex3 = 1.23 + 2.80
print(round(ex3, 2))        # prints 4.03 so rounds to 2 decimal places