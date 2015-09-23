"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

def calculate():
    """Runs calculator, takes no arguments

    Prompt user for operation, call function imported from arithmetic,
    and print result.
    """
    while True: 
        prompt = "Enter an operation or enter 'q' to quit."
        num_to_calc = raw_input(prompt)
        if num_to_calc.lower() == 'q': #if the first token is Q, quit
            return
        else:
            tokens = num_to_calc.split()
            # check validity of input
            if len(tokens) == 3:
                func_name = tokens[0]
                num1 = int(tokens[1])
                num2 = int(tokens[2])
            elif len(tokens) == 2: 
                func_name = tokens[0]
                num1 = int(tokens[1])
                num2 = 1
            else:
                print "That is not a valid entry."
                continue # go to the top of the while loop


            # create a dictionary with keys = operations
            # make global and pass to calculate???
            operations = {'+': add(num1, num2),
                          '-': subtract(num1, num2),
                          '*': multiply(num1, num2),
                          '/': divide(num1, num2),
                          'square': square(num1),
                          'cube': cube(num1),
                          'pow': power(num1, num2),
                          'mod': mod(num1, num2)}
                                                    
            # retrieve and call operation from dict
            if func_name in operations:
                print operations[func_name]

            # if func_name == "+":
            #     print add(num1, num2)
            # elif func_name == '-':
            #     print subtract(num1, num2)
            # elif func_name == 
calculate()