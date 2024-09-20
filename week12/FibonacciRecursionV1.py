"""FibonacciRecursionV1"""
def fibonacci(num):
    """fibonanci"""
    if not num:
        return 0
    if num == 1:
        return 1
    return fibonacci(num-1)+fibonacci(num-2)

def main(num):
    """main"""
    print(fibonacci(num))
main(int(input()))
