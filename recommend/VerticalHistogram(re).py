"""VerticalHistogram"""
def main():
    """main"""
    text = list(input())
    text.sort()
    data = {}
    for i in text:
        if i.isalpha():
            if i in data:
                data[i] += 1
            else:
                data[i] = 1
    most_value = max(data.values())
    for i in range(most_value,0,-1):
        print(f"{i:>2}  ",end="")
        for j in data.values():
            if j >= i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    print("    ",end = "")
    print(" ".join(data))
main()
