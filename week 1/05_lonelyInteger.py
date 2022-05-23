#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    if (len(a) == 1):
        return a[0]

    n = len(a)
    key = None
    
    for i in range(n):
        key = a[i]
        for j in range(n):
            if (i==j):
                continue
                
            if (key == a[j]):
                key = None
                break
        if(key!=None):
            return key

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
