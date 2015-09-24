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
    token_list = "'+' '-'' '*' '/' 'square' 'cube' 'pow' 'or' 'mod'"
    print "Enter an operation or enter 'q' to quit."
    print "Valid operations include {}".format(token_list)

    while True: 
        num_to_calc = raw_input("> ")
        if num_to_calc.lower() == 'q': #if the first token is Q, quit
            return
        else: 
            tokens = num_to_calc.split()
        if len(tokens) < 2 or len(tokens) > 3:
            print "That is not a valid entry."
            continue
        func_name = tokens[0]
        try: 
            num1 = float(tokens[1])
        except ValueError:
            print "That is not a valid entry."
            continue
        if len(tokens) > 2:
            num2 = float(tokens[2])
        else:
            num2 = 1

        if func_name == '+':
            print add(num1, num2)
        elif func_name == '-':
            print subtract(num1, num2)
        elif func_name == '*':
            print multiply(num1, num2)
        elif func_name == '/':
            print divide(num1, num2)
        elif func_name == 'square':
            print square(num1)
        elif func_name == 'cube':
            print cube(num1)
        elif func_name == 'pow':
            print power(num1, num2)
        elif func_name == 'mod':
            print mod(num1, num2)
        else:
            print "First element must be one of the following:"  
            print token_list
            continue 

            # # check validity of input
            # if len(tokens) == 3:
            #     func_name = tokens[0]
            #     num1 = float(tokens[1])
            #     num2 = float(tokens[2])
            # elif tokens[0] == 'square' or tokens[0] == 'cube':

            # else:
            #     print "That is not a valid entry."
            #     continue # go to the top of the while loop


            # create a dictionary with keys = operations
            # make global and pass to calculate???
            # operations = {'+': add(num1, num2),
            #               '-': subtract(num1, num2),
            #               '*': multiply(num1, num2),
            #               '/': divide(num1, num2),
            #               'square': square(num1),
            #               'cube': cube(num1),
            #               'pow': power(num1, num2),
            #               'mod': mod(num1, num2)}
                                                    
            # retrieve and call operation from dict
            # if func_name in operations:
            #     print operations[func_name]

            # if func_name == "+":
            #     print add(num1, num2)
            # elif func_name == '-':
            #     print subtract(num1, num2)
            # elif func_name == 
calculate()