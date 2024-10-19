"""Sock"""
def main():
    """main"""
    sock_count = {}
    lst_sock = []
    pair_sock = []
    data = input()
    for i in data:
        if i not in sock_count:
            sock_count[i] = 1
        else:
            sock_count[i] += 1
    for key,value in sock_count.items():
        if value % 2:
            sock_count[key] -= 1
        lst_sock.append(sock_count[key] * key)
        lst_sock.sort()
    for i in lst_sock:
        for j in range(0, len(i) ,2):
            pair_sock.append(i[j:j+2])
    count = len(pair_sock)
    x = " ".join(pair_sock)
    if not count:
        print("None")
        print(count)
        return
    print(x)
    print(count)
main()
