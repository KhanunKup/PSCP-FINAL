"""GCD_v1&v2"""
def gcd(a, b):
    """GCD"""
    if not b:
        return a
    return gcd(b, (a % b))

def main(num1,num2):
    """main""" 
    most = max(num1,num2)
    least = min(num1,num2)
    print(gcd(most,least))
main(int(input()),int(input()))
