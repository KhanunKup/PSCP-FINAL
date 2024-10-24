"""Bus Seat"""
def main():
    """main"""
    row = int(input()) # even only
    col = int(input())
    target = int(input())
    count = 0
    for i in range(row,0,-1):
        if count == 2:
            print()
            count = 0
        for _ in range(col):
            if i == target:
                print("XX" ,end = " ")
                i += row
                continue
            print(f"{i:>02}", end = " ")
            i += row
        print()
        count += 1
main()
