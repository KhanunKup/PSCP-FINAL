"""Easy Histogram No Dict.py"""
def main():
    """main"""
    text = input()
    alpha = {}
    for i in text:
        if i in alpha:
            alpha[i] += 1
        else:
            alpha[i] = 1
    sort_alpha = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"
    for i in sort_alpha:
        if i in alpha:
            print(f"{i} = {alpha[i]}")
main()
