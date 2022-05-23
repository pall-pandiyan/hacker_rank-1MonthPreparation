#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    hour = s[:2]
    amOrPm = s[8:]
    if (amOrPm == "AM"):
        if ( hour == "12" ):
            hour = "00"
    else:
        if ( hour != "12" ):
            hourInt = int(hour)
            hourInt = hourInt + 12
            hour = str(hourInt)

    s = hour + s[2:8]
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
