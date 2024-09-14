"""WordSequence I"""
def main():
    """main"""
    text = input()
    for i in range(len(text)):
        print(text[:i+1])
main()
