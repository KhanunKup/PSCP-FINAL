"""Debaratna"""
def main():
    """main"""
    road = float(input())
    if 0 <= road <= 5.032:
        print("Bangkok")
    elif 5.032 < road <= 35.477:
        print("Samut Prakarn")
    elif 35.477 < road <= 52.9:
        print("Chachoengsao")
    elif 52.9 < road <= 58.855:
        print("Chon Buri")
    else:
        print("InValid")
main()
