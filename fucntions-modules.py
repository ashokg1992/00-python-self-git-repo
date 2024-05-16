

############################### #######         FUNCTONS #################### #######################

# FUNCTION:
# ------------
# insted of writing same code again and again in source code , just we write that code as a function and call it when it is necesary.




# Benefits of Functions and Modules:

#     Reusability: Functions allow you to write code once and use it multiple times.

#     Modularity: Modules help in organizing code into logical units, making it easier to manage.

#     Abstraction: Functions allow you to focus on what a piece of code does rather than how it does it.

#     Readability: Well-defined functions and modules make code more understandable.

#     Testing and Debugging: Functions and modules facilitate easier testing and debugging of code segments.

#     Collaboration: Modules enable multiple programmers to work on different parts of a project simultaneously.

# Remember to give your functions and modules descriptive names and include comments or docstrings to explain their purpose and usage. This makes your code more understandable and maintainable.

# Using functions and modules is a best practice in Python programming and contributes to writing clean, efficient, and organized code.


# ###########################  writing function ##########################

# we write function with nmae "def"
# def greet(name):    # we define funciton with name of "greet" and in that function we can write anyting
#     print(f"hello,{name}")
# greet("ashok")
# greet ("kumar")

# ///////////////////ADDITION USING FUNCTION //////////////////////

# def addition(x,y):
#     return(x+y) 
# print(addition(3,4))
# print(addition(789,456))

# like this we write code one time, and use it anywhere by just calling it 

#######################################################

# def is_even(num):
#     return num % 2 == 0
# def is_odd(num):
#     return num % 2 != 0
# def square(num):
#     return num ** 2 
# # test functions now
# num=int(input("enter input"))
# if is_even(num):
#     print (f"{num} is even")
# else:
#     print (f"{num} is odd")
# print (f"the  square of{num} is {square(num)}")


###################################### MODULES ######################################

# import modulesforfunctions
# a=modulesforfunctions.add(2,3)
# print(a)
# print(modulesforfunctions.add(5,6))  # we call in anyway
# print(f"the additionof value is {modulesforfunctions.add(5,6)}")  # we call  it by using FORMATED STRING FOR BETTER LOOK


# import modulesforfunctions

# result_add = modulesforfunctions.add(3, 4)
# result_subtract = modulesforfunctions.subtract(7, 2)

# print(result_add)     # Output: 7
# print(result_subtract)  # Output: 5


#/////////////////////////////  importing specific  functions from moudle //////////////////////

# from modulesforfunctions import multiply, divide

# result_multiply = multiply(5, 6)
# result_divide = divide(8, 2)

# print(result_multiply)  # Output: 30
# print(result_divide)    # Output: 4.0


#########################################################################################


def add(x,y):
    return(x+y)
def sub(x,y):
    return(x-y)
def multi(x,y):
    return(x*y)
def div(x,y):
    return(x/y)
# now we define these function under this file , now these funcltins are to be used in another file  
 
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"