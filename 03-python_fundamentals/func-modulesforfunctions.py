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