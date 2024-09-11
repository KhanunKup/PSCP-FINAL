"""pringles"""
def main():
    """process"""
    top = input() # top of box
    chips = input() # potato chips in box
    bot = input() # bottom of box
    count = 0
    reach_count = 0
    reach = int(input()) # how far we can reach?
    for i in chips: # count potato chips
        if i == ")":
            count += 1
    chip = chips[:max(0,reach)] # how much can we picked it up.
    for j in chip:
        if j == ")":
            reach_count += 1
    if count > reach_count: # potato chips still remiain in box
        print(reach_count)
        print("There are still some left.")
        print(top)
        x = chips.replace(")"," ",reach_count) # replace spacebar
        print(x)
        print(bot)
    else: # nothing left
        print(count)
        print("None.")
        print(top)
        y = chips.replace(")"," ",reach_count) # replace spacebar
        print(y)
        print(bot)
main()
