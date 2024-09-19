"""VerticalHistogram"""
def main():
    """main"""
    alpha_dict = {}
    data = input()
    data = list(data)
    data.sort()
    new_data = []
    for i in data: # count frequency of letter
        if i.isalpha():
            alpha_dict[i] = alpha_dict.get(i,0) + 1
    most_value = max(alpha_dict.values())
    for i in data: # list of unique char
        if i.isalpha() and i not in new_data:
            new_data.append(i)
    n = 0
    for _ in range(most_value):
        sequnce = most_value - n
        print(f"{sequnce:>2} " ,end ="") # frequncy bar
        for count in alpha_dict.values():
            if count >= sequnce:
                print(" *" ,end = "")
            else:
                print("  " ,end = "")
        n += 1
        print()
    print("    "+" ".join(alpha_dict)) # data bar
main()
