"""Majority"""
def main(candidate,amount):
    """main"""
    dic_can = {x : 0 for x in range(1,candidate+1)}
    for _ in range(amount):
        vote = int(input())
        dic_can[vote] += 1
    max_key = max(dic_can, key=dic_can.get)
    max_value = dic_can[max_key]
    if max_value < amount/2:
        max_key = 0
    print(max_key,max_value)
main(int(input()),int(input()))
