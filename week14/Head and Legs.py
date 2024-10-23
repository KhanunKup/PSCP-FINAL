"""Head and Legs"""
def main():
    """main"""
    a = int(input()) # all animal
    b = int(input()) # all legs
    x = (b-2*a)//2
    y = (4*a-b)//2
    if x < 0 or y < 0 or b != 4*x + 2*y:
        print("Impossible")
        return
    print(int(x) , int(y))
main()
