"""
The best python module ever. 
"""

import numpy as np

def print_value(value):
    print value

def FizzBuzz_function(lowerRange,upperRange):
    # FizzBuzz function prints the numbers from 1 to 100. But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz"
    # Input: lowerRange, upperRange
    # Output: None
    
    """
    Docstrings are fun!
    """
    
    for i in np.arange(lowerRange,upperRange):

        if i%3 == 0 and i%5 != 0:
            print "Fizz"
        if i%5 == 0 and i%3 != 0:
            print "Buzz"
        if i%5 == 0 and i%3 == 0:
            print "FizzBuzz"

        else: 
            print i
 