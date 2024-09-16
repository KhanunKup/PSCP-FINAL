"""Safe"""
def main():
    """main"""
    key = []
    text_lst = []
    count = 0
    text = input()
    key_lock = input()
    for i in text:
        text_lst.append(ord(i))
    for i in key_lock:
        key.append(ord(i))
    i = 0
    for n in range(len(text)):
        base1 = key[n]
        base2 = key[n]
        while True:
            if base1 == text_lst[n] or base2 == text_lst[n]:
                count += i
                i = 0
                break
            base1 += 1
            base2 -= 1
            i += 1
            if base1 > 90:
                base1 = 65
            if base2 < 65:
                base2 = 90
    print(count)
main()
