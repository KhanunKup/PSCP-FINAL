"""BreachTheDoor"""
def main():
    """main"""
    ar_sort = ""
    list_sort = []
    text = input()
    for i in text:
        if i.isalpha():
            ar_sort += i
        if i.isspace():
            ar_sort += " "
    ar_sort = ar_sort.split()
    for i in ar_sort:
        if len(i) > 6:
            list_sort.append(i)
    for i in list_sort:
        print(i,end = " ")
main()
