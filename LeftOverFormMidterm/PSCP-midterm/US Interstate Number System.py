"""US RAHHHHHHH"""
def main(num):
    """main"""
    lenght = len(str(num))
    if lenght in (1,2):
        if lenght == 2 and str(num)[1] == "0":
            print("Horizontal Major Interstate")
            print(f"I-{num}")
        elif lenght == 1 and num == 5:
            print("Vertical Major Interstate")
            print(f"I-{num}")
        elif lenght == 2 and str(num)[1] == "5":
            print("Vertical Major Interstate")
            print(f'I-{num}')
        else:
            print("Others")
    elif lenght == 3:
        check = str(num)[0]
        if not int(str(num)[1:]):
            print("Others")
        elif not int(check) % 2 and str(num)[2] in ("0","5"):
            print("Even Minor Interstate")
            print(f'I-{int(str(num)[1:])}')
        elif int(check) % 2 and str(num)[2] in ("0","5"):
            print("Odd Minor Interstate")
            print(f'I-{int(str(num)[1:])}')
        else:
            print("Others")
    else:
        print("Others")
main(int(input()))
