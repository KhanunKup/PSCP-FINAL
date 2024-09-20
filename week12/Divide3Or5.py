"""Divide3Or5"""
def divide_by(num):
    """divide by 3 or 5"""
    if not num %3 or not num%5:
        return num
    return 0

def main(num):
    """main"""
    count = 0
    for i in range(num+1):
        count += divide_by(i)
    print(count)
main(int(input()))
