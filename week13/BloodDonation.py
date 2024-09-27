"""BloodDonation"""
def main():
    """main"""
    condition = True
    age = int(input())
    weight = int(input())
    count = int(input())
    if 17 >age >70:
        condition = False
    if weight < 45:
        condition = False
    if age > 55 and count < 1:
        condition = False
    if age == 17 or 60 <= age <= 70:
        paper = input()
        if not paper:
            condition = False
    if condition:
        print("Yes")
        return
    print("No")
main()
