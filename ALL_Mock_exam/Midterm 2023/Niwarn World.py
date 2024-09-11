"""Niwarn World"""
import math
def xfunction(n):
    """calculate X"""
    x = 2+(math.log(n**2,2)/(2*n*math.log(n,2)))
    return x

def yfunction(n,s):
    """calculate Y"""
    y = (math.sin(math.radians(30))+math.sqrt(2*s))/(xfunction(n)+3)
    return y

def zfunction(k):
    """calculate Z"""
    z = (yfunction(k,k)**2)+(8456*(xfunction(k))**4)/(24*k)
    return z

def main(n,s,k):
    """main"""
    result1 = xfunction(n)
    result2 = yfunction(n,s)
    result3 = zfunction(k)
    print(f"X: {result1:.1f}, Y: {result2:.1f}, Z: {result3:.1f}")
main(float(input()),float(input()),float(input()))
