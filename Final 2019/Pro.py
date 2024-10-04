"""Pro"""
def main(come,pay,price,ry_come):
    """main"""
    if ry_come >= come:
        promo_count = ry_come // come # who in promo
        remain = ry_come % come # who isn't
        total_promo = promo_count * pay
        print((remain+total_promo)*price)
    else:
        print(ry_come*price)
main(int(input()),int(input()),int(input()),int(input()))
