"""Home run"""
def main(count,distant):
    """main"""
    result = 0
    for _ in range(count):
        size = float(input())
        if distant > size:
            result += 1
    print(result)
main(int(input()),float(input()))
