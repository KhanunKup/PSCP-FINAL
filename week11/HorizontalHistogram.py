"""HorizontalHistogram"""
def main():
    """main"""
    dic_alpha = {}
    sorted_text = []
    text = input()
    for i in text:
        sorted_text.append(i)
    sorted_text.sort()
    sorted_text.sort(key=str.isupper) # upper behide lowwer
    for i in sorted_text:
        if i in dic_alpha:
            dic_alpha[i] += 1
        else:
            dic_alpha[i] = 1
    for i,count in dic_alpha.items():
        hypen = ""
        for j in range(count):
            if j > 0 and not j % 5:
                hypen += "|"
            hypen += "-"
        print(f"{i} : {hypen}")
main()
