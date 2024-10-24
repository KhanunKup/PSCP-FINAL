"""Diamond I"""
def main():
    """main"""
    row = int(input())
    col = int(input())
    all_line = []
    vertical_line = []
    cal = []
    for _ in range(row):
        data = input().split()
        all_line.append(data)
    for i in range(col):
        for j in range(row):
            data = int(all_line[j][i])
            cal.append(data)
        vertical_line.append(sum(cal))
        cal.clear()
    print(max(vertical_line))
main()
