"""Books"""
import math
def main(ea,page_ea):
    """main"""
    base = page_ea
    x = int(input())
    y = int(input())
    i = 0
    count = 0
    while True:
        if ea < 1:
            break
        page_per_day = math.ceil(base *((x+i) /(y+i)))
        if base - page_per_day < 1:
            count += ea
            break
        page_ea -= page_per_day
        i += 1
        count += 1
        if page_ea < 1:
            ea -= 1
            page_ea = base
    print(count)
main(int(input()),int(input()))
