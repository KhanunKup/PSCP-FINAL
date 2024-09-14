"""MissingCard No Set"""
def main():
    """main"""
    sp = ["AS","KS","QS","JS","10S","9S","8S","7S","6S","5S","4S","3S","2S"]
    he = ["AH","KH","QH","JH","10H","9H","8H","7H","6H","5H","4H","3H","2H"]
    di = ["AD","KD","QD","JD","10D","9D","8D","7D","6D","5D","4D","3D","2D"]
    cl = ["AC","KC","QC","JC","10C","9C","8C","7C","6C","5C","4C","3C","2C"]
    card_list = sp + he + di + cl
    ip_list = []
    for _ in range(51):
        card = input()
        ip_list.append(card)
    for i in card_list:
        if i not in ip_list:
            print(i)
main()
