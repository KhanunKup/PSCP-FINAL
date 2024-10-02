"""isprime_small"""
def is_prime(num):
    """isprime"""
    if num in (0,1):
        return "False"
    if num == 2:
        return "True"
    for i in range(3,int((num**0.5))+1,2): # decrease range of num
        if not num % i:
            return "False"
    return "True"

def main(num):
    """main"""
    print(is_prime(num))
main(int(input()))
