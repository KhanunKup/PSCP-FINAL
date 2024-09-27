"""Matrix"""
def main(m,n):
    """main"""
    data = []
    for _ in range(m*n):
        data.append(input())
    for _ in range(m):
        for _ in range(n):
            print(data[0] ,end=" ")
            data.remove(data[0])
        print()
main(int(input()),int(input()))
