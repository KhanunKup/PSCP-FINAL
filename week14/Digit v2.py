"""Digit v2"""
def main():
    """main"""
    digit = 1
    data = input().split()
    digit1 = ("ten","eleven","twelve")
    for i in data:
        if i[len(i)-4:len(i)+1] == "sand":
            if digit <4:
                digit = 4
        elif i[len(i)-3:len(i)+1] == "red":
            if digit <3:
                digit = 3
        elif i[len(i)-2:len(i)+1] == "ty":
            if digit <2:
                digit = 2
        elif i[len(i)-4:len(i)+1] == "teen":
            if digit <2:
                digit = 2
        elif i in digit1:
            if digit <2:
                digit = 2
    print(digit)
main()
