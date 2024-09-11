"""MAC"""
def main():
    """main function""" # this code is fcking dirty
    hypen_cnt = False
    colon_cnt = False
    dot_cnt = False
    result = ""
    new_ip = ":"
    valid_alpha = ["a","b","c","d","e","f","0","1","2","3","4","5","6","7","8","9"]
    ip = input()
    if not ip.find("-") == -1 and len(ip) == 17:
        hypen_cnt = True
        new_ip = ip.replace("-","")
    elif not ip.find(":") == -1 and len(ip) == 17:
        new_ip = ip.replace(":","")
        colon_cnt = True
    elif not ip.find(".") == -1 and len(ip) == 14:
        new_ip = ip.replace(".","")
        dot_cnt = True
    for i in new_ip: # check valid alpha
        i = i.lower()
        if i not in valid_alpha:
            print("ERROR")
            return
    if hypen_cnt:
        result = '-'.join([new_ip[i:i+2] for i in range(0, len(new_ip), 2)])
        if result == ip:
            print("VALID 1")
            return
    elif colon_cnt:
        result = ':'.join([new_ip[i:i+2] for i in range(0, len(new_ip), 2)])
        if result == ip:
            print("VALID 2")
            return
    elif dot_cnt:
        result = '.'.join([new_ip[i:i+4] for i in range(0, len(new_ip), 4)])
        if result == ip:
            print("VALID 3")
            return
    print("ERROR")
main()
