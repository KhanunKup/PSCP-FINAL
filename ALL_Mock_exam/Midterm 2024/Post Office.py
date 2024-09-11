"""Post Office"""
def main():
    """main"""
    cost = 0
    envelop = int(input())
    package = int(input())
    for _ in range(envelop):
        weight1 = float(input())
        if 0 <= weight1 <= 10:
            cost += 29
        if 10 < weight1 <= 20:
            cost += 31
        if 20 < weight1 <= 100:
            cost += 36
        if 100 < weight1 <= 250:
            cost += 41
        if 250 < weight1 <= 500:
            cost += 46
        if 500 < weight1 <= 1000:
            cost += 61
        if 1000 < weight1 <= 2000:
            cost += 81
    for _ in range(package):
        weight2 = float(input())
        if 0 <= weight2 <= 500:
            cost += 60
        if 500 < weight2 <= 1000:
            cost += 70
        if 1000 < weight2 <= 2000:
            cost += 85
    print(cost)
main()
