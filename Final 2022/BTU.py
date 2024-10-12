"""BTU"""
def vol_cal(vol):
    """vol_cal"""
    btu_count = 0
    match vol:
        case vol if 100 <= vol <= 150:
            btu_count = 5000
        case vol if 151 <= vol <= 250:
            btu_count = 6000
        case vol if 251 <= vol <= 300:
            btu_count = 7000
        case vol if 301 <= vol <= 350:
            btu_count = 8000
        case vol if 351 <= vol <= 400:
            btu_count = 9000
        case vol if 401 <= vol <= 450:
            btu_count = 10000
        case vol if 451 <= vol <= 550:
            btu_count = 12000
        case vol if 551 <= vol <= 700:
            btu_count = 14000
        case vol if 701 <= vol <= 1000:
            btu_count = 18000
        case vol if 1001 <= vol <= 1200:
            btu_count = 21000
        case vol if 1201 <= vol <= 1400:
            btu_count = 23000
        case vol if 1401 <= vol <= 1500:
            btu_count = 24000
        case vol if 1501 <= vol <= 2000:
            btu_count += 30000
        case vol if 2001 <= vol <= 2500:
            btu_count += 34000
    return btu_count

def main():
    """main"""
    vol = int(input())
    height = int(input())
    people = int(input()) # can 0
    room_type = input()
    heat = input()
    btu_count = 0
    btu_count += vol_cal(vol)
    btu_count += max((height-8),0) * 1000
    btu_count += max((people-2),0) * 600
    if room_type == "kitchen":
        btu_count += 4000
    if heat == "facing the sun":
        btu_count = btu_count * 1.1
    if heat == "shaded":
        btu_count = btu_count * 0.9
    print(int(btu_count))
main()
