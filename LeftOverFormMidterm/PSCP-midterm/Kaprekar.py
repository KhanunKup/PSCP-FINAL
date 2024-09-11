"""kaprekar"""
def rejust_num(num1,num2,num3,num4):
    """so_rt_num"""
    if num1 < num2:
        num1, num2 = num2, num1
    if num1 < num3:
        num1, num3 = num3, num1
    if num1 < num4:
        num1, num4 = num4, num1
    if num2 < num3:
        num2, num3 = num3, num2
    if num2 < num4:
        num2, num4 = num4, num2
    if num3 < num4:
        num3, num4 = num4, num3
    return str(num1)+str(num2)+str(num3)+str(num4), str(num4)+str(num3)+str(num2)+str(num1)

def main():
    """input"""
    count = 1
    num = input()
    while True:
        num1 = int(num[0])
        num2 = int(num[1])
        num3 = int(num[2])
        num4 = int(num[3])
        result_high , result_low = rejust_num(num1,num2,num3,num4)
        result = int(result_high) - int(result_low)
        result = str(result)
        num = result.rjust(4,"0")
        if num == "6174":
            break
        count += 1
    print(count)
main()
