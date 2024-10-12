"""WPM"""
def kids_cal(speed):
    """kids"""
    if speed <11:
        return "Very Slow"
    if 11 <= speed <= 20:
        return "Slow"
    if 21 <= speed <= 30:
        return "Average"
    if 31 <= speed <= 40:
        return "Fast"
    if speed > 40:
        return "Very Fast"
    return None

def adults_cal(speed):
    """kids"""
    if speed <26:
        return "Very Slow"
    if 26 <= speed <= 35:
        return "Slow/Beginner"
    if 36 <= speed <= 45:
        return "Intermediate/Average"
    if 46 <= speed <= 65:
        return "Fast/Advanced"
    if 66 <= speed <= 80:
        return "Very Fast"
    if speed > 80:
        return "Insane"
    return None

def main():
    """main"""
    age = input()
    speed = int(input())
    if age == "Kids":
        print(kids_cal(speed))
    else:
        print(adults_cal(speed))
main()
