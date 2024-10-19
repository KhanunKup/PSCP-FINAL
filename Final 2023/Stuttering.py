"""Stuttering"""
def main():
    """main"""
    mem = ""
    result = ""
    data = input().split()
    for i in data:
        if mem == i:
            continue
        result += i + " "
        mem = i
    print(result)
main()
