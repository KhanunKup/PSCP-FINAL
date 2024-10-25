"""Music Lover"""
def main():
    """main"""
    music = {}
    n = int(input())
    for _ in range(n):
        data = input().strip()
        data = data.split("-")
        if data[0] not in music:
            music[data[0]] = []
        music[data[0]].append(data[-1])
    for key,value in music.items():
        print(key)
        for i in value:
            print(i)
main()
