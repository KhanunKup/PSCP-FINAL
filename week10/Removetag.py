"""removetag"""
def main():
    """main"""
    tag_removed = ""
    condition = True
    tag = input().split()
    for i in tag:
        for j in i:
            if j == "<":
                condition = False
                continue
            if j == ">":
                condition = True
                tag_removed += " "
                continue
            if condition:
                tag_removed += j
        tag_removed += " "
    print(tag_removed.split())
main()
