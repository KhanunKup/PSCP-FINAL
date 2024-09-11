"""Coffee"""
def main(a,b,c,d,e):
    """main"""
    totalbill = a*e
    condition1 = (a*(e-(e-1)))+(a*(1-(b/100))*(e-1))
    condition2 = a*(1-(c/100))*e
    if totalbill >= d:
        pass
    else:
        condition2 = totalbill
    if condition1 > condition2:
        print(2)
        print(f"{condition2:.2f}")
    if condition1 < condition2:
        print(1)
        print(f"{condition1:.2f}")
    if condition1 == condition2:
        print(2)
        print(f"{condition2:.2f}")
main(float(input()),float(input()),float(input()),float(input()),int(input()))
