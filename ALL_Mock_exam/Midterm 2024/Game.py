"""Game"""
def main():
    """main"""
    num1 = int(input())
    num2 = int(input())
    if num1%3 == num2%3:
        print(num1%3)
    else:
        print("Error")
main()
