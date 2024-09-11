"""fully pair"""
def main():
    """main"""
    counter_string = ""
    result = ""
    text = input()
    for i in text:
        if counter_string.count(i) < 1:
            counter_string += i
    for j in counter_string:
        if text.count(j) %2:
            result += j
    if not result:
        print("fully paired")
    else:
        print(result)
main()
