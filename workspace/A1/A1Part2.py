import sys
import os
from scipy.io.wavfile import read
from scipy.io.wavfile import write
sys.path.append('../../software/models/')
from utilFunctions import wavread

"""
A1-Part-2: Basic operations with audio

Write a function that reads an audio file and returns the minimum and the maximum values of the audio 
samples in that file. 

The input to the function is the wav file name (including the path) and the output should be two floating 
point values returned as a tuple.

If you run your code using oboe-A4.wav as the input, the function should return the following output:  
(-0.83486432, 0.56501967)
"""
def minMaxAudio(inputFile):
    """
    Input:
        inputFile: file name of the wav file (including path)
    Output:
        A tuple of the minimum and the maximum value of the audio samples, like: (min_val, max_val)
    """

    dataIn = wavread(inputFile)
    fs0 = dataIn[0]
    x = dataIn[1]

    max_val = max(x)
    min_val = min(x)

    # bOutput = True
    # validationOutput(bOutput,max_val,min_val)

    return (min_val,max_val)

# def validationOutput(bOutput,max_val,min_val):
#     """
#     Input:
#         bOutput: whether to output code-validation information
#     Output:
#         Code-validation information
#     """
#     if (bOutput):
#         print 'min_val: '
#         print '%.9f' % min_val
#
#         print 'max_val: '
#         print '%.9f' % max_val
#
#     return
#
# inputFile_ = "/home/alex/Documents/sms-tools/sounds/oboe-A4.wav"
# minMaxAudio(inputFile_)