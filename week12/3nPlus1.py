"""3nPlus1"""
def recursive(number ,count = 0):
    """recursive"""
    if number == 1:
        return count
    if not number %2:
        return recursive(number//2,count +1)
    return recursive(number * 3 +1,count +1)

def main():
    """main"""
    while True:
        number = abs(int(input()))
        if not number:
            break
        count = recursive(number)
        print(count+1)
main()
