# calculator_tkinter.py

import tkinter as tk
from tkinter import messagebox

def add(x, y):
    """Add two numbers"""
    return x + y

def subtract(x, y):
    """Subtract two numbers"""
    return x - y

def multiply(x, y):
    """Multiply two numbers"""
    return x * y

def divide(x, y):
    """Divide two numbers"""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

def calculate():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        operator = operator_var.get()

        if operator == "+":
            result = add(num1, num2)
        elif operator == "-":
            result = subtract(num1, num2)
        elif operator == "*":
            result = multiply(num1, num2)
        elif operator == "/":
            result = divide(num1, num2)

        result_label.config(text=f"Result: {result:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numbers.")

root = tk.Tk()
root.title("Simple Calculator")

num1_label = tk.Label(root, text="Number 1:")
num1_label.pack()

num1_entry = tk.Entry(root)
num1_entry.pack()

operator_var = tk.StringVar()
operator_var.set("+")

operator_menu = tk.OptionMenu(root, operator_var, "+", "-", "*", "/")
operator_menu.pack()

num2_label = tk.Label(root, text="Number 2:")
num2_label.pack()

num2_entry = tk.Entry(root)
num2_entry.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack()

result_label = tk.Label(root, text="Result:")
result_label.pack()

root.mainloop()












'''# calculator.py

def add(x, y):
    """Add two numbers"""
    return x + y

def subtract(x, y):
    """Subtract two numbers"""
    return x - y

def multiply(x, y):
    """Multiply two numbers"""
    return x * y

def divide(x, y):
    """Divide two numbers"""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

def main():
    print("Simple Calculator")
    print("----------------")

    while True:
        num1 = input("Enter the first number: ")
        try:
            num1 = float(num1)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        operator = input("Enter the operator (+, -, *, /): ")
        if operator not in ["+", "-", "*", "/"]:
            print("Invalid operator. Please enter +, -, * or /.")
            continue

        num2 = input("Enter the second number: ")
        try:
            num2 = float(num2)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if operator == "+":
            result = add(num1, num2)
        elif operator == "-":
            result = subtract(num1, num2)
        elif operator == "*":
            result = multiply(num1, num2)
        elif operator == "/":
            result = divide(num1, num2)

        print(f"{num1} {operator} {num2} = {result:.2f}")

        response = input("Do you want to continue? (y/n): ")
        if response.lower()!= "y":
            break

if __name__ == "__main__":
    main()'''