"""fourdirection"""
def main():
    """main"""
    line = 1
    direct = input()
    for _ in range(5):
        for i in direct:
            match line:
                case 1:
                    print("  *  ",end =" ")
                case 2:
                    match i:
                        case "L":
                            print(" *   ", end=" ")
                        case "R":
                            print("   * ", end=" ")
                        case "U":
                            print(" *** ", end=" ")
                        case "D":
                            print("  *  ", end=" ")
                case 3:
                    match i:
                        case "L":
                            print("*****", end=" ")
                        case "R":
                            print("*****", end=" ")
                        case "U":
                            print("* * *", end=" ")
                        case"D":
                            print("* * *", end=" ")
                case 4:
                    match i:
                        case"L":
                            print(" *   ", end=" ")
                        case "R":
                            print("   * ", end=" ")
                        case "U":
                            print("  *  ", end=" ")
                        case "D":
                            print(" *** ", end=" ")
                case 5:
                    print("  *  ",end =" ")
        print()
        line += 1
main()
