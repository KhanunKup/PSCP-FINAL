"""PickThemAgain"""
def main():
    """main"""
    data = input().split()
    data.reverse()
    check = []
    for i in data:
        i = int(i)
        if not i%3 or not i%5:
            check.append(i)
    if not check:
        print("Nope")
    for i in check:
        print(i)
main()
