"""Bookworm"""
def main():
    """main"""
    total_time = []
    timecount = 0
    count = 0
    data_count = int(input())
    for _ in range(data_count):
        read_time = float(input())
        ea_book = int(input())
        for _ in range(ea_book):
            time_per_book = float(input())
            total_time.append(time_per_book)
            total_time.sort() # most important part
        for i in total_time:
            timecount += i
            if timecount <= read_time:
                count +=1
        print(count)
        total_time.clear()
        timecount = 0
        count = 0
main()
