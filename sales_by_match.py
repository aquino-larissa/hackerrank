import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def unique(ar):
    color_dict = {}
    for elem in ar:
        if color_dict.get(elem, "null") == "null":
            color_dict[elem] = 1
        else:
            color_dict[elem] += 1
    return color_dict

def sockMerchant(n, ar):
    n_pair = 0
    unique_colors = unique(ar)
    for color in unique_colors:
        n_pair += int((unique_colors[color] - unique_colors[color]%2)/2)
    return n_pair

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
