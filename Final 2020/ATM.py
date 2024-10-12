"""ATM"""
def main():
    """main"""
    cash = int(input())
    while True:
        action = input()
        if action == "END":
            break
        if action[0] == "D":
            cash += int(action[2:])
        if action[0] == "W":
            if cash - int(action[2:]) < 0:
                cash = 0
                continue
            cash -= int(action[2:])
    print(cash)
main()
