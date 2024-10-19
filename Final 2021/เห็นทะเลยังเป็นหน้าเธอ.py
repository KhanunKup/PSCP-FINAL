"""เห็นทะเลยังเป็นหน้าเธอ"""
def main():
    """main"""
    data = input()
    twilight = ["CHAIN CAT","GREAT WHITE","GUMMY","BLUE","MAKO"]
    midnight = ["FRILLED","GOBLIN","SIXGILL","GREENLAND","COOKIECUTTER"]
    abyssal = ["MEGAMOUTH"]
    if "SHARK" not in data:
        print("ZONE JAI MA KLUNG RAK DUAY KAN MAI.")
        return
    data = data.replace(" SHARK","")
    if data == "BULL":
        print("THE SHALLOW ZONE")
    elif data in twilight:
        print("THE TWILIGHT ZONE")
    elif data in midnight:
        print("THE MIDNIGHT ZONE")
    elif data in abyssal:
        print("THE ABYSSAL ZONE")
main()
