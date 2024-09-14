"""MissingNumber"""
def main(round_):
    """main"""
    list_ = []
    round_list = []
    diff = []
    while True:
        num = int(input())
        if not num:
            break
        list_.append(num)
    for i in range(1,round_+1):
        round_list.append(i)
    for i in round_list:
        if i not in list_:
            diff.append(i)
    diff.sort()
    for i in diff:
        print(i)
main(int(input()))
