import math
from math import log
def calc_log(a, b):
    result = 0
    if b.isdigit():
        result = math.log(a, int(b))
    else:
        result = math.log(a)

    return result

first_num = int(input())
second_num = input()

print(f"{calc_log(first_num, second_num):.2f}")
