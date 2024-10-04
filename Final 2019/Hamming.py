"""Hamming"""
def main(text1,text2):
    """main"""
    count = 0
    text1 = list(text1)
    text2 = list(text2)
    for index,value in enumerate(text1):
        if value != text2[index]:
            count += 1
    print(count)
main(input(),input())
