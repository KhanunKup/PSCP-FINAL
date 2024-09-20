"""All_Primes"""
def is_prime(n):
    """isprime"""
    if n in (0,1):
        return False
    if n == 2:
        return True
    for i in range(2,n):
        if not n % i:
            return False
    return True

def main(num):
    """main"""
    count = 0
    for n in range(num+1):
        if is_prime(n):
            count += 1
    print(count)
main(int(input()))
