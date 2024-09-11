"""Median"""
import math
def main(): # this code is fckiing dirty bro.
    """aaah"""
    mean = []
    num = int(input())
    if not num%2:
        for _ in range(num):
            n = float(input())
            mean.append(n)
        median = (num+1) / 2
        floor = math.floor(median)-1
        ceil = math.ceil(median)-1
        mean.sort()
        total = (mean[floor]+mean[ceil])/2
        print(f"{total:.3f}")
    else:
        for _ in range(num):
            n = float(input())
            mean.append(n)
        median = ((num+1) / 2) -1
        median = int(median)
        mean.sort()
        print(f"{mean[median]:.3f}")
main()
