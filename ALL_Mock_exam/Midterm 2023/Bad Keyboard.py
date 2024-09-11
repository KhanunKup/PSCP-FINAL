"""Bad Keyboard"""
def main():
    """main"""
    x = "IOio"
    y = "OIoi"
    text = input()
    tran = str.maketrans(x,y)
    print(text.translate(tran))
main()
