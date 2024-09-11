"""tuple sad life"""
def main():
    """main"""
    tuple_text = input().split()
    tuple_text = tuple(tuple_text)
    num = input()
    find_tuple = tuple_text.index(num)
    if not find_tuple:
        print(0)
    else:
        count_tuble = tuple_text.count(num)
        if count_tuble <= 1:
            print(find_tuple)
        else:
            for _ in range(count_tuble):
                for _ in range(count_tuble):
                    print(find_tuple, end = " ")
                print()
main()
