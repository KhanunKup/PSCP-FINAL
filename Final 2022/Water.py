"""Water"""
def main():
    """main"""
    n = int(input()) # month
    a = float(input()) # baht per unit
    b = float(input()) # if over unit
    c = float(input()) # baht per unit of over
    d = float(input()) # if under baht
    total = 0
    cal = 0
    for _ in range(n):
        used = float(input())
        if used <= b:
            cal += used * a
        elif used > b:
            cal += ((used - b) * c) + (b * a)
        if cal <= d:
            continue
        total += cal
        cal = 0
    print(f"{total:.2f}")
main()
