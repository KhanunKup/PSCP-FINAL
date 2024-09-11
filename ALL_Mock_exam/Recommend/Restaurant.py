"""restaurant"""
def main(price,promo,discount,option):
    """process"""
    dis = 1-(discount/100)
    totalbill = price + option #บิลรวม
    newmustpay = totalbill * dis #ราคาที่ต้องจ่ายหลังเข้าโปร
    discountprice = price * dis #ลดราคา ver เข้าโปรเลย
    if not newmustpay: #ไม่ซื้อเพิ่ม
        print("Yes")
    elif not option: #ไม่ซื้อเพิ่ม
        print("Yes")
    elif price == promo: #เข้าโปรอยู่เเล้ว
        if newmustpay > discountprice:
            print(f"No {newmustpay-discountprice:.3f}")
    elif totalbill >= promo:
        if newmustpay < price: #ลดราคาเเล้วจ่ายน้อยกว่าเดิม
            mustpay = price - newmustpay
            print(f"Yes {mustpay:.3f}") 
        elif newmustpay > price: #ลดเเล้วมากกว่าเดิม
            mustpay = newmustpay - price
            print(f"No {mustpay:.3f}")
        elif newmustpay == price:  #ลดเเล้วเท่าเดิม เเต่ได้กินเพิ่ม คุ้ม..
            print("Yes")
main(float(input()),float(input()),float(input()),float(input()))
