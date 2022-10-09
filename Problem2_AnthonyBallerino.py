#LINK 1 https://www.hackerrank.com/challenges/birthday-cake-candles - Birthday cake candles___________________________________________________________________________________________
#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    max_height = 0
    for candle in candles:
        if candle > max_height:
            max_height = candle
    count = 0
    for candle in candles:
        if candle == max_height:
            count += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
#LINK 2 https://www.hackerrank.com/challenges/kangaroo - Number line jumps___________________________________________________________________________________________
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    k_one_p = x1
    k_two_p = x2
    k_one_j = v1
    k_two_j = v2
    progress_1 = k_one_p - k_one_j
    progress_2 = k_two_p - k_two_j
    answer = ""
    sign = progress_1*progress_2
    if progress_1 % progress_2 == 0 and sign >= 0:
        if k_one_p != 0 and k_two_p != 0:
            answer = "YES"
    else:
        answer = "NO"
    return(answer)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(str(result) + '\n')

    fptr.close()
#LINK 3 ___________________________________________________________________________________________
#LINK 4 ___________________________________________________________________________________________
#LINK 5 ___________________________________________________________________________________________
#LINK 6 __________________________________________________________________________________________