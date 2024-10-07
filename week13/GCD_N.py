"""GCD_N"""
import math
from functools import reduce
def gcd_cal(lst_num):
    """gcd_cal"""
    return reduce(math.gcd,lst_num) # make gcd can take more 2 parameter

def main(num):
    """main"""
    lst_num = [int(input()) for _ in range(num)]
    print(gcd_cal(lst_num))
main(int(input()))
