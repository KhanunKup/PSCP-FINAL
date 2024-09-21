"""OneTwo"""
def recursive(num):
    """recursive"""
    if num == 1:
        return "1"
    if num == 2:
        return "2"
    return recursive(num-1) + recursive(num-2)

def main(num):
    """main"""
    print(recursive(num))
main(int(input()))
