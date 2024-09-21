"""CaesarV1"""
def main():
    """main"""
    decode = ""
    encode = int(input())
    text = input()
    for i in text:
        if i.isalpha():
            if i.isupper():
                result = ord(i) + encode
                while result >90:
                    result -= 26
                while result <65:
                    result += 26
            if i.islower():
                result = ord(i) + encode
                while result >122:
                    result -= 26
                while result <97:
                    result += 26
        else:
            result = ord(i)
        decode += chr(result)
    print(decode)
main()
