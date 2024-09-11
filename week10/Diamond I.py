"""Diamond"""
def main(m,n):
    """main"""
    all_line = []
    frist_digit = []
    most_value = []
    for _ in range(m):
        txt = input().split()
        all_line.append(txt)
    for j in range(n): # create a list of verticle line
        for i in range(m):
            verticle = int(all_line[i][j])
            frist_digit.append(verticle)
        most_value.append(sum(frist_digit)) # add value of verticle line
        frist_digit.clear()
    print(max(most_value))
main(int(input()),int(input()))
