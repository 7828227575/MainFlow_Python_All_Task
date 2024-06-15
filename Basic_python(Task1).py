'''
TASK-1:
        Basic Python Syntax Understanding
Description:
        The intern will learn foundational Python
        concepts such as variables, data types, loops,
        and functions.
Responsibility:
        1. Study Python syntax through tutorials and
        simple coding exercises.
        2. Practice writing basic scripts to perform
        arithmetic operations, manipulate strings,
        and use conditional statements.
        3.Gain familiarity with common data structures
        like lists, dictionaries, and tuples.
'''

# Variables and Data Types
# Assign a value to a variable
x = 5  # integer
y = 3.14  # float
name = "Sachin "  # string

# Print the values
print(x)  # Output: 5
print(y)  # Output: 3.14
print(name)  # Output: Sachin 



# Basic Arithmetic Operations
# Addition
result = x + 2
print(result)  # Output: 7

# Subtraction
result = x - 2
print(result)  # Output: 3

# Multiplication
result = x * 2
print(result)  # Output: 10

# Division
result = x / 2
print(result)  # Output: 2.5


# String Manipulation
# Concatenate strings
greeting = "Hello, " + name
print(greeting)  # Output: Hello, Sachin 

# Upper case
print(name.upper())  # Output: SACHIN

# Lower case
print(name.lower())  # Output: sachin


# Conditional Statements
# If-Else Statement
if x > 10:
    print("x is greater than 10")
else:
    print("x is less than or equal to 10")
# Output: x is less than or equal to 10


# Loops
# For Loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Output:
# apple
# banana
# cherry

# While Loop
i = 0
while i < 5:
    print(i)
    i += 1
# Output:
# 0
# 1
# 2
# 3
# 4


# Functions
# Define a function
def greet(name):
    print("Hello, " + name)

# Call the function
greet("Sachin")
# Output: Hello, Sachin


# Data Structures
# Lists
numbers = [1, 2, 3, 4, 5]
print(numbers[0])  # Output: 1
print(numbers[-1])  # Output: 5

# Dictionaries
person = {"name": "Sachin", "age": 24}
print(person["name"])  # Output: Sachin
print(person["age"])  # Output: 24

# Tuples
colors = ("red", "green", "blue")
print(colors[0])  # Output: red
print(colors[-1])  # Output: blue