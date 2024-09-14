"""Easy Histogram No Dict.py"""
def main():
    """main"""
    text = input()
    text_list = []
    one_i = []
    for i in text:
        if not i.isspace():
            text_list.append(i)
    text_list = sorted(sorted(text_list, reverse=True), key=str.lower)
    for i in text_list:
        if i not in one_i:
            one_i.append(i)
    for i in one_i:
        print(f"{i} = {text_list.count(i)}")
main()
