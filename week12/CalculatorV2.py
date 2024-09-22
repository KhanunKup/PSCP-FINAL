# """CalculatorV2"""
# def main(num):
#     """main"""
#     result = ""
#     # plus symbol = number -1
#     for i in range(1,num+1):
#         result += str(i) + "+"
#     print(len(result))
# main(int(input()))

# manaul check ^^^^

"""CalculatorV2"""
def main(num):
    """main"""
    total_presses = 0
    digit_length = 1
    current_number = 1
    if num <= 1:
        print(1)
        return
    while current_number <= num:
        # หาจำนวนตัวเลขที่มี digit_length หลัก
        next_number = min(num + 1, 10 ** digit_length)
        count = next_number - current_number
        # คำนวณจำนวนการกด: ตัวเลขในช่วงนั้น × จำนวนหลัก
        total_presses += count * digit_length
        # เลื่อนไปช่วงตัวเลขที่มีหลักถัดไป
        current_number = next_number
        digit_length += 1
    print(total_presses + num)
main(int(input()))
