"""Bonus"""
def main(current,year,month):
    """main"""
    if month >= 10:
        year += 1
    if year >= 20:
        year = 20
    current *= year
    if current <= 5000:
        current = 5000
    elif current >= 1000000:
        current = 1000000
    print(current)
main(int(input()),int(input()),int(input()))
