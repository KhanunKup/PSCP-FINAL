"""Alcohol"""
def main():
    """main"""
    consume = 0
    gender = input()
    weight = float(input())
    paper = input()
    volume_per_can = float(input())
    alcohol_per_can = float(input())
    amount = int(input())
    rest = int(input())
    consume =  ((volume_per_can * alcohol_per_can)/100) * amount
    blood = 0
    if gender == "Male":
        blood = consume/(weight*0.68*10) - (rest * 0.015)
    else:
        blood = consume/(weight*0.55*10) - (rest * 0.015)
    if blood > 0.05 or paper == "No":
        print("Not Safe")
    else:
        print("Safe")
main()
