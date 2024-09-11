"""Longer"""
import math
def main(r,a,b):
    """main"""
    text = "Equal"
    circle = 2*math.pi*r
    squr = 2*(a+b)
    if circle > squr:
        result = circle - squr
        text = "Circle is longer"
        print(text)
        print(f"{result:.5f}")
    elif circle < squr:
        result = squr - circle
        text = "Rectangle is longer"
        print(text)
        print(f"{result:.5f}")
    else:
        result = circle - squr
        print(text)
        print(f"{result:.5f}")
main(float(input()),float(input()),float(input()))
