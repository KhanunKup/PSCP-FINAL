"""LastStand"""
import json
def main():
    """main"""
    data = json.loads(input())
    for i in data:
        print(str(i)[-1])
main()
