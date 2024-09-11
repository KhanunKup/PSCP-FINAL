"""Point Sorting"""
def function_sort(data):
    """I don't know how to use lambda bro"""
    x = int(data[0])
    y = int(data[-1])
    return x + y, -y
def main(num1):
    """main"""
    cor_list = []
    for _ in range(num1):
        num2 = int(input())
        for _ in range(num2):
            data = input()
            cor_list.append(data.split())
        cor_list.sort(key=function_sort)
        for i in cor_list:
            print(" ".join(i))
        cor_list.clear()
main(int(input()))
