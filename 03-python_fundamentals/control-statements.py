
# a = input("hi user, enter your  name: ")
# print ('user  entered  name:',a)


# a = int(input("hi user, enter your  name: "))
# print ('user  entered  name:',a)                  $ if you enter  non integer , then i/p is invalid if you give "int" as input

# a = float(input("hi user, enter your  name: "))
# print ('user  entered  name:',a)                   # other than float it give error


# @@@@@@@@@@@@ QUESTION @@@@@@@@@@@@@@@@@@

# HOW YOU TAKE INPUT FROM USER?
#  by using input method as shown above
 
#  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# age=22
# if age>= 18:
#     print("user is adult")
# else:
#     print("user is not adult")
 

# age=10
# if age>= 18:
#     print("user is adult")
# else:
#     print("user is not adult")
    
    
# age=int(input("enter your age: "))
# if age>= 18:
#     print("user is adult")
# else:
#     print("user is not adult")


############################################  IF - ELIF #############################################

# score=int(input("enter your scor "))
# if score >= 90:
#     print("user is distinction")
# elif score >= 80:
#     print("user is grade-B")
# elif score >= 70:
#     print("grade-c")
# else:
#     print ("user is fail")
   
    

 
############################################  IF - nested-if #############################################

# x=30   # 30,10,40
# y=20
# if x>y:
#     print (" x is greater than y")
#     if x >30:
#         print("x is greater than 30")
#     else:
#         print ("x is not grater than 30")
# else:
#     print(" x is not greater than y")
           

#################################  loop - for #################################################

# fruits=['apple', 'banan', 'cherry']
# for x in fruits:
#     print(x)
    
    
#################################  loop - while   #################################################
# until conditionils to be fila , it is exeuted


# x=0
# while x <= 10:
#     print (x)
#     x += 1

# x=10
# while x <= 101:
#     print (x)
#     x += 1
           
# count =0
# while count <= 10:
#     print (count)
#     count += 1



#################################  break - continue  #################################################

# for i in range(10):
#     if i ==5:
#         break
#     print (i)


# for i in range(10):
#     if i ==5:
#        continue
#     print (i)




#################################  dictionary  #################################################

# person= {'name':'ashok', 'age':'30', 'city':'bangalkore'}
# for key,value  in person.items():
#     print(f'{key}:{value}')


#################################  else  with out break #################################################

# for i in range(10):
#     print(i)
# else:
#     print("loop exited with out a break")


#################################   break  inside for loop  #################################################

# for i in range(5):
#     if i == 3:
#         break  
#         #print     # here print is not valid, under "if" we write print blkock
#     print(i)
# else:
#     print("loop exited with out a break")
 


#################################  SAMPLE EXAMPLS  #################################################

## SAMPLE PROGRAM

# Certainly! Below is a sample Python program that demonstrates user inputs, control statements (if-else), and loops (for loop and while loop):

# ```python
# # User inputs
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))

# # Control statement (if-else)
# if age >= 18:
#     print(f"Hello {name}! You are eligible to vote.")
# else:
#     print(f"Hello {name}! You are not yet eligible to vote. You can vote in {18 - age} years.")

# # For loop
# print("Printing numbers from 1 to 5 using a for loop:")
# for i in range(1, 6):
#     print(i)

# # While loop
# num = int(input("Enter a number: "))
# fact = 1
# i = 1

# while i <= num:
#     fact *= i
#     i += 1

# print(f"The factorial of {num} is: {fact}")
# ```

# This program does the following:

# 1. Takes user inputs for `name` and `age`.
# 2. Uses an `if-else` statement to check if the user is eligible to vote based on their age.
# 3. Prints numbers from 1 to 5 using a `for` loop.
# 4. Calculates the factorial of a number using a `while` loop.

# Here's an example of how the program would work:

# ```
# Enter your name: Alice
# Enter your age: 22
# Hello Alice! You are eligible to vote.
# Printing numbers from 1 to 5 using a for loop:
# 1
# 2
# 3
# 4
# 5
# Enter a number: 5
# The factorial of 5 is: 120
# ```

# This program showcases the use of user inputs, control statements (if-else), and loops (for loop and while loop) in Python.



