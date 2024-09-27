"""Pongya"""
def main(num):
    """main"""
    if not int(num) % 3 or num[-1] == "3":
        print("PONG")
    else:
        print(num)
main(input())
