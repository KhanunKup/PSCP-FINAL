"""shorten"""
def main():
    """main"""
    result = ""
    start = None
    end = None
    while True:
        num = int(input())
        if num == -1:
            break
        if start is None:
            start = num
            end = num
        elif num == end + 1:
            end = num
        else:
            if start == end:
                result += f"{start}, "
            else:
                result += f"{start}-{end}, "
            start = num
            end = num
    if start is not None:
        if start == end:
            result += f"{start}"
        else:
            result += f"{start}-{end}"
    print(result)
main()
