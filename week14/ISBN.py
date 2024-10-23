"""ISBN"""
def main():
    """main"""
    num = 0
    count = 10
    data = input().replace("-","")
    last_num = data[-1]
    data = data[::-1]
    data = data.replace(last_num,"",1)
    data = data[::-1]
    for i in data:
        num += int(i) * count
        count -= 1
    num *= -1
    check = num % 11
    if check == 10 and last_num == "X":
        print("Yes")
        return
    if check == 10:
        print("No X")
        return
    if check == int(last_num):
        print("Yes")
        return
    print("No",check)
main()
