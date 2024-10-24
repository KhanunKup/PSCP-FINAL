"""Flatten"""
def main():
    """main"""
    data = input()
    number = []
    result = ""
    for i in data:
        if i.isnumeric() or i == "-":
            result += i
        else:
            if result:
                number.append(int(result))
            result = ""
    number.sort(reverse=True)
    print(number)
main()
