"""TicTacToe"""
def main():
    """main"""
    line_1 = list(input())
    line_2 = list(input())
    line_3 = list(input())
    for i in range(3): # vertical
        x_win_ver = line_1[i] + line_2[i] + line_3[i]
        o_win_ver = line_1[i] + line_2[i] + line_3[i]
        if x_win_ver == "XXX":
            print("X WIN")
            return
        if o_win_ver == "OOO":
            print("O WIN")
            return

    # horizon
    if line_1 == ["X", "X", "X"] or line_2 == ["X", "X", "X"] or line_3 == ["X", "X", "X"]:
        print("X WIN")
        return
    if line_1 == ["O", "O", "O"] or line_2 == ["O", "O", "O"] or line_3 == ["O", "O", "O"]:
        print("O WIN")
        return

    if line_1[0] == line_2[1] == line_3[2] == "X" or line_1[2] == line_2[1] == line_3[0] == "X":
        print("X WIN")
        return
    if line_1[0] == line_2[1] == line_3[2] == "O" or line_1[2] == line_2[1] == line_3[0] == "O":
        print("O WIN")
        return
    print("DRAW")
main()
