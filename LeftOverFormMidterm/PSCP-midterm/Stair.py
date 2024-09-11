"""Stair"""
def main():
    """main"""
    current_position = 0
    step_up = 0
    lenght = int(input())
    step = int(input())
    heights = [int(input()) for _ in range(step)]
    while current_position < step:
        next_position = current_position
        while next_position < step and sum(heights[current_position:next_position + 1]) <= lenght:
            next_position += 1
        if next_position == current_position:
            print("NO")
            return
        step_up += 1
        current_position = next_position
    print(step_up)
main()
