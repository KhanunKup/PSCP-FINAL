"""Hello"""
def main():
    """main"""
    mem = ""
    status = False
    conso = ("a","e","i","o","u")
    data = input()
    for i in data:
        if i in conso:
            status = True
            mem = i
    if not status:
        print(data)
        return
    data = data[::-1]
    data = data.replace(mem,mem*4,1)
    data = data[::-1]
    print(data)
main()
