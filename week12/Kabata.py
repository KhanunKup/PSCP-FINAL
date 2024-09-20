"""Kabata"""
def main(num):
    """main"""
    for _ in range(num):
        lang = input()
        if lang.find("baka") >= 0:
            print("no")
            continue
        lang = lang.replace("bakka","")
        lang = lang.replace("ka","")
        lang = lang.replace("ta","")
        lang = lang.replace("ba","")
        if not lang:
            print("yes")
        else:
            print("no")
main(int(input()))
