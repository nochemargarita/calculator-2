"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""
# function that tokenizes input str
# function calculator_loop

from arithmetic import *


# Your code goes here
def tokenize_input(input_str):
    """this will return the split input str"""
    return input_str.split(" ")


def calculator():
    """Performs different arithmetic based on user input."""
    while True:
        user_input = raw_input("Enter desired arithmetic: ")
        tokens = tokenize_input(user_input)
        if tokens[0] == "q" or tokens[0] == "quit":
            return
        else:
            if tokens[0] == "+":
                print add(float(tokens[1]), float(tokens[2]))
            elif tokens[0] == "-":
                print subtract(float(tokens[1]), float(tokens[2]))
            elif tokens[0] == "*":
                print multiply(float(tokens[1]), float(tokens[2]))
            elif tokens[0] == "/":
                print divide(float(tokens[1]), float(tokens[2]))
            elif tokens[0] == "square":
                print square(float(tokens[1]))
            elif tokens[0] == "cube":
                print cube(float(tokens[1]))
            elif tokens[0] == "pow":
                print power(float(tokens[1]), float(tokens[2]))
            elif tokens[0] == "mod":
                print mod(float(tokens[1]), float(tokens[2]))
            else:
                print "Please enter valid command."


calculator()
