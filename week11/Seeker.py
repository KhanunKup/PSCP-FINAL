"""Seeker"""
def main():
    """main"""
    lst_num = []
    data = input()
    count = ""
    result = 0
    for i in data: # find num in data
        if i.isnumeric():
            count += i
        else:
            lst_num.append(count)
            count = ""
    lst_num.append(count)
    for i in lst_num:
        if i.isnumeric(): # find num in lst
            result += int(i)
    print(result)
main()
