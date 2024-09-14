"""Duplicate I"""
def main(num1,num2):
    """main"""
    list_num1 = []
    list_num2 = []
    diff = []
    for _ in range(num1):
        text_id = input()
        list_num1.append(text_id)
    for _ in range(num2):
        text_id = input()
        list_num2.append(text_id)
    for i in list_num1:
        for j in list_num2:
            if i == j:
                diff.append(j)
    diff.sort(reverse=True)
    if not diff:
        print("Nope")
    for i in diff:
        print(i)
main(int(input()),int(input()))
