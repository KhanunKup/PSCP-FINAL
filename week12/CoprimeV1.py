"""CoprimeV1"""
def gcd(a,b):
    """gcd"""
    if not b:
        return a
    return gcd(b, (a % b))

def main():
    """main"""
    num1 = int(input())
    num2 = int(input())
    most = max(num1,num2)
    least = min(num1,num2)
    co_gcd = gcd(most,least)
    if co_gcd == 1:
        print("YES")
    else:
        print("NO")
    print(co_gcd)
main()
