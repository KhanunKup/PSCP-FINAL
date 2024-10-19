"""Taking Turns"""
import json
def main():
    """main"""
    data = json.loads(input())
    new_data = []
    if not len(data):
        print(data)
        return
    x = data.pop(len(data)-1)
    new_data.append(x)
    while len(data) != 0:
        for _ in range(2):
            if not len(data):
                break
            x = data.pop(0)
            new_data.append(x)
        for _ in range(2):
            if not len(data):
                break
            x = data.pop(len(data)-1)
            new_data.append(x)
    print(new_data)
main()
