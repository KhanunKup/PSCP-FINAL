"""Fever"""
def checktemp(temp):
    """checktemp"""
    if 38 <= temp <39:
        return "Mild Fever"
    if 39 <= temp <40:
        return "High Fever"
    if temp >=40:
        return "Very High Fever"
    return "No Fever"
def main(temp):
    """main"""
    print(checktemp(temp))
main(float(input()))
