"""MultiplyMatrixPQR"""
def main():
    """main"""
    p = int(input())
    q = int(input())
    r = int(input())
    a = []
    b = []
    ab = []
    for _ in range(p*q):
        data = int(input())
        a.append(data)
    for _ in range(q*r):
        data = int(input())
        b.append(data)
    
main()
