"""foodgrade"""
def main(round_= 24,count = 0):
    """main"""
    if not round_:
        print(count)
        return
    weight = float(input())
    if 50 <= weight <= 70:
        count += 1
    main(round_ - 1,count)
main()
