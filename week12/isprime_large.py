"""isprime_small"""
def is_prime(num):
    """isprime"""
    if num in (0,1):
        return "NO"
    if num == 2:
        return "YES"
    for i in range(2,int((num**0.5))+1): # decrease range of num
        if not num % i:
            return "NO"
    return "YES"

def main(num):
    """main"""
    print(is_prime(num))
main(int(input()))
