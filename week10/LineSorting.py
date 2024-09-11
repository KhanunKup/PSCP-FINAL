"""lineSorting"""
def main():
    """main"""
    txt_list = []
    num = int(input())
    for _ in range(num):
        txt = input()
        txt_list.append(txt)
    txt_list.sort(key=len)
    for i in txt_list:
        print(i)
main()
