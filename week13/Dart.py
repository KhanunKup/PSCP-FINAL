"""Dart"""
def main(amount):
    """main"""
    point = 0
    for _ in range(amount):
        locate = input().split()
        dis = ((int(locate[0])**2)+(int(locate[1])**2))**0.5
        if dis <= 2:
            point += 5
        elif dis <= 4:
            point += 4
        elif dis <= 6:
            point += 3
        elif dis <= 8:
            point += 2
        elif dis <= 10:
            point += 1
    print(point)
main(int(input()))
