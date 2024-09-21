"""Day2011"""
def main(date,month):
    """main"""
    year = 2011
    if month < 3:
        month += 12
        year -= 1
    k = year %100
    j = year //100
    day = (date + (13*(month+1))//5 + k +(k//4) +(j//4)-2*j) % 7
    days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    print(days[day])
main(int(input()),int(input()))
