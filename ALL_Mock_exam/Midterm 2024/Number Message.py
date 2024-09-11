"""Number Message"""
def main():
    """main"""
    condition = False
    result = ""
    text = input()
    for i in text:
        if i == "1":
            result += "I"
            condition = True
        elif i == "3":
            result += "E"
            condition = False
        elif i == "4":
            result += "A"
            condition = False
        elif i == "5":
            result += "S"
            condition = False
        elif i == "0":
            result += "O"
            condition = False
        elif i.isnumeric():
            if i == "2" and condition:
                result += "R"
                condition = False
            else:
                result += ""
                condition = False
        else:
            result += i.upper()
            condition = False
    result = result.replace("IR","R")
    result = result.replace("IE","B")
    print(result)
main()
