"""Difference"""
def main():
    """main"""
    set_n = set()
    set_m = set()
    n = int(input())
    m = int(input())
    for _ in range(n):
        num = int(input())
        set_n.add(num)
    for _ in range(m):
        num = int(input())
        set_m.add(num)
    z = set_n - set_m
    z = sorted(z)
    for i in z:
        print(i, end = " ")
main()
