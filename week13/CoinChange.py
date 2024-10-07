"""CoinChange"""
def main(coin):
    """main"""
    count = 0
    lst_coin = [25,10,5,1]
    i = 0
    while True:
        if not coin:
            break
        if coin - lst_coin[i] >= 0:
            coin -= lst_coin[i]
            count += 1
        else:
            i += 1
    print(count)
main(int(input()))
