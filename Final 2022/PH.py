"""Ph"""
def cal_ph(ph):
    """cal_ph"""
    if ph == 7:
        return "neutral"
    if 7 <ph <=14:
        return "akaline"
    if 0 <= ph < 7:
        return "acidic"
    return "error"

def main():
    """main"""
    ph = float(input())
    print(cal_ph(ph))
main()
