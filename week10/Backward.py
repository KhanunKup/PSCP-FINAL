"""backward"""
def main():
    """main"""
    text = ""
    list_text = []
    while True:
        text = input()
        if text == "NULL":
            break
        list_text.append(text)
    i = -1
    for _ in list_text:
        print(list_text[i])
        i -= 1
main()
