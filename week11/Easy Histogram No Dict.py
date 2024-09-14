"""Easy Histogram No Dict.py"""
def main():
    """main"""
    text = input()
    text_list = []
    number = {}
    for i in text: # create a sorted list
        if not i.isspace():
            text_list.append(i)
    text_list = sorted(sorted(text_list,reverse=True),key=str.lower) # most important part 
    for i in text_list:
        if i in number:
            number[i] += 1
        else:
            number[i] = 1
    for i in number: # use i  to traverse in dict(keys)
        print(f"{i} = {number[i]}") 
main()
