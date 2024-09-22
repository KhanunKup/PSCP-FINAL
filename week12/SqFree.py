"""SqFree"""
import math
def sqfree(num):
    """sqfree"""
    for i in range(2, int(math.sqrt(num)) +1):
        if not num % (i * i):
            return False
    return True

def main(number):
    """main"""
    result = 0
    for i in range(1,number+1):
        count = sqfree(i)
        if count:
            result += 1
    print(result)
main(int(input()))
