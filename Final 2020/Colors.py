"""Colors"""
def main():
    """main"""
    col1 = input()
    col2 = input()
    if col1 == "Red" and col2 == "Yellow":
        print("Orange")
    elif col2 == "Red" and col1 == "Yellow":
        print("Orange")
    elif col1 == "Red" and col2 == "Blue":
        print("Violet")
    elif col2 == "Red" and col1 == "Blue":
        print("Violet")
    elif col1 == "Yellow" and col2 == "Blue":
        print("Green")
    elif col2 == "Yellow" and col1 == "Blue":
        print("Green")
    elif col2 == "Red" and col1 == "Red":
        print("Red")
    elif col2 == "Yellow" and col1 == "Yellow":
        print("Yellow")
    elif col2 == "Blue" and col1 == "Blue":
        print("Blue")
    else:
        print("Error")
main()
