"""isprime_small"""
def is_prime(num):
    """isprime"""
    if num in (0,1):
        return "No"
    if num == 2:
        return "Yes"
    for i in range(2,num):
        if not num % i:
            return "No"
    return "Yes"

def main(num):
    """main"""
    print(is_prime(num))
main(int(input()))
