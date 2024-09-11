"""IT Business"""
def main(account_start,start):
    """main"""
    count_ = 0
    while True:
        if count_ >= 3:
            break
        text = input()
        if text == "end":
            break
        money = float(text[2:])
        if text.count("D"):
            if start - money < 0:
                count_ += 1
                continue
            account_start += money
            start -= money
            count_ = 0
        else:
            if account_start - money < 0:
                count_ += 1
                continue
            start += money
            account_start -= money
            count_ = 0
    print(f"{account_start:.2f}")
    print(f"{start:.2f}")
main(float(input()),float(input()))
