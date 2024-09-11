"""Amefuri"""
def time_check(time):
    """check time"""
    if 6 <= time < 18:
        return "Day"
    return "Night"
def main():
    """main"""
    wet_level = 8
    time = int(input())
    text = input()
    text_lower = text.lower()
    for i in text_lower:
        if time >= 24:
            time = 0
        current_time = time_check(time)
        if wet_level <= 0:
            print("Dry")
            return
        if wet_level >= 16:
            wet_level = 16
        match current_time:
            case "Day":
                match i:
                    case "c":
                        wet_level -= 0.50
                        time += 1
                    case "n":
                        wet_level -= 1.00
                        time += 1
                    case "w":
                        wet_level -= 1.50
                        time += 1
                    case "r":
                        wet_level += 2.00
                        time += 1
                    case "s":
                        wet_level += 3.00
                        time += 1
                    case "h":
                        print("Lost")
                        return
            case "Night":
                match i:
                    case "c":
                        wet_level -=0.25
                        time += 1
                    case "n":
                        wet_level -=0.50
                        time += 1
                    case "w":
                        wet_level -=0.75
                        time += 1
                    case "r":
                        wet_level += 2.00
                        time += 1
                    case "s":
                        wet_level += 3.00
                        time += 1
                    case "h":
                        print("Lost")
                        return
    if wet_level > 0:
        print(f"Still Wet (Wet Level: {wet_level:.2f})")
    else:
        print("Dry")
main()
