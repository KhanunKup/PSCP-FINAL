"""Cat Parade"""
def main():
    """main"""
    cat_list =[]
    sorted_catlist = []
    index_sorted = []
    while True:
        text = input()
        if text == "END":
            break
        if text == "IT'S A DOG": # remove dog info
            if cat_list:
                cat_list.pop()
        else:
            cat_list.extend(text.split(", ")) # create a sorted list
    for i in cat_list:
        sorted_catlist.append(i)
    for i in sorted_catlist:
        if i not in index_sorted:
            index_sorted.append(i)
    index_sorted.sort()
    for i in index_sorted:
        count_index = sorted_catlist.index(i)
        count_value = sorted_catlist.count(i)
        print(f"{i} {count_index+1} {count_value}")
main()
