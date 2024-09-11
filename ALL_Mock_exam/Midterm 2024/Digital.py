"""digital"""
def main(name,reg,home,old,income,money):
    """main"""
    check = reg in("Yes","True") and home in("Yes","True")
    hf = "receive a digital wallet amount of 10,000 baht, sponsored by all taxpayers in Thailand."
    if check and (old >= 16 and income <= 840000 and money <=500000):
        print(f"Congratulations! {name} is qualified to {hf}")
    else:
        print(f"Unfortunately, {name} is not qualified.")
main(input(),input(),input(),float(input()),float(input()),float(input()))
