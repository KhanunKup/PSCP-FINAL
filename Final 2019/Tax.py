"""Tax"""
def cal_cc(cc):
    """cal_cc"""
    total = 0
    if cc >= 1801:
        total = (cc - 1800)*4 + 2100
    elif cc >= 601:
        total = (cc - 600)*1.5 + 300
    elif cc <= 600:
        total = cc * 0.5
    return total

def main():
    """main"""
    old = int(input())
    cc = int(input())
    pay_cc = cal_cc(cc)
    if old >= 10:
        pay_cc = pay_cc * 0.5
    elif old == 9:
        pay_cc = pay_cc * 0.6
    elif old == 8:
        pay_cc = pay_cc *0.7
    elif old == 7:
        pay_cc = pay_cc *0.8
    elif old == 6:
        pay_cc = pay_cc *0.9
    print(f"{pay_cc:.2f}")
main()
