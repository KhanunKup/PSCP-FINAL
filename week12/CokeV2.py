"""Coke V2"""
import math
def main(price,promo,spec,want):
    """main"""
    if not promo: # no promotion
        total = want * price
    elif not want: # no buy
        total = 0
    else:
        total = ((price*want)-(math.ceil((want-promo)/promo)*(price-spec)))
    print(total)
main(int(input()),int(input()),int(input()),int(input()))
