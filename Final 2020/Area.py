"""Area"""
def main():
    """main"""
    count = 0
    row_count = int(input())
    for _ in range(row_count):
        text = input()
        for i in text:
            if i.isspace():
                continue
            count += 1
    print(count)
main()
