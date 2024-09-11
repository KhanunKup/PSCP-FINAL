"""passwoed"""
import math
def main():
    """main"""
    alpha = 0
    upperalpha = 0
    num = 0
    symbol = 0
    text = input()
    for i in text:
        if i.islower():
            alpha = 26
        if i.isupper():
            upperalpha = 26
        if i.isnumeric():
            num = 10
        if i in ("~","`","!","@","#","$","%","^","&","*","(",")","-","_","+","=","{","}","[","]"):
            symbol = 32
        if i in ("|","\\","/",":",";","<",">",",",".","?"):
            symbol = 32
    sigma = alpha + upperalpha + num + symbol
    long = len(text)
    result = math.log(sigma**long,2)
    print(math.floor(result))
    if math.floor(result) < 28:
        print("Very Weak")
    if 28 <= math.floor(result) <= 35:
        print("Weak")
    if 36<= math.floor(result)<= 59:
        print("Reasonable")
    if 60 <= math.floor(result)<= 127:
        print("Strong")
    if math.floor(result) >= 128:
        print("Very Strong")
main()
