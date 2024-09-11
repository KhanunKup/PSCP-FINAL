"""Lift"""
def main(amount,limit_weight):
    """main"""
    status = False
    count_weight = 0
    for _ in range(amount):
        age = int(input())
        weight = float(input())
        if age >= 12:
            status = True
        count_weight += weight
    if (count_weight <= limit_weight and status) or not amount:
        print("Safe")
    else:
        print("Not Safe")
main(int(input()),float(input()))
