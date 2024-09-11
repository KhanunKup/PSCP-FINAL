"""Real"""
def main():
    """main"""
    result = ""
    for i in range(1,25):
        status = input()
        if status == "off":
            if i in(8,16,24):
                result += ","
            else:
                result += "0"
        else: #on
            if i in(8,16,24):
                result += "."
            else:
                result += "1"
    result = result.replace("1111110","0")
    result = result.replace("0110000","1")
    result = result.replace("1101101","2")
    result = result.replace("1111001","3")
    result = result.replace("0110011","4")
    result = result.replace("1011011","5")
    result = result.replace("1011111","6")
    result = result.replace("1110000","7")
    result = result.replace("1111111","8")
    result = result.replace("1111011","9")
    result = result.replace(",","")
    if len(result) >6 or result.count(".")> 1 :
        print("Error")
    else:
        print(f"{float(result):.2f}")
main()
