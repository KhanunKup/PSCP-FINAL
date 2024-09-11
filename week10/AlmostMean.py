"""Almostmean"""
def main(num):
    """main"""
    result = ""
    total = 0
    id_list = []
    score_list = []
    for _ in range(num):
        text = input()
        result += text + " "
    result = result.split()
    # for i in range(len(result)): #split into two list
    for i,value in enumerate(result): #split into two list
        if not i % 2:
            id_list.append(value)
        else:
            score_list.append(float(value))
    for i in score_list: # find average
        total += i
    avg = total/num
    closest = max(x for x in score_list if x <= avg)# find closest
    find_closest = score_list.index(closest)
    print(f"{id_list[find_closest]}\t{score_list[find_closest]}")
main(int(input()))
