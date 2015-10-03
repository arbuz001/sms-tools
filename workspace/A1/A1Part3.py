import numpy as np

# import sys
# import os
# sys.path.append('../../software/models/')
# from utilFunctions import wavread

"""
A1-Part-3: Python array indexing

Write a function that given a numpy array x, returns every Nth element in x, starting from the 
first element.  

The input arguments to this function are a numpy array x and a positive integer N such that N < number of 
elements in x. The output of this function should be a numpy array.

If you run your code with x = np.arange(10) and N = 2, the function should return the following output: 
array([0, 2, 4, 6, 8]).
"""


def hopSamples(x, N):
    """
    Inputs:
        x: input numpy array
        N: a positive integer, (indicating hop size)
    Output:
        A numpy array containing every Nth element in x, starting from the first element in x.
    """
    # method 1

    y = x[::N]

    # bOutput = True
    # validationOutput(bOutput, y)

    return y


def validationOutput(bOutput, y):
    """
    Input:
        bOutput: whether to output code-validation information
    Output:
        Code-validation information
    """
    if (bOutput):
        np.set_printoptions(10)
        print 'y: '
        print y

    return

# x_ = np.arange(10)
# N = 2
# hopSamples(x_,N)