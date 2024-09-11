"""GradeIII"""
def main():
    """main"""
    num = int(input())
    total = 0
    for _ in range(num):
        score = float(input())
        if 95 <= score <=100:
            total += 4
        if 90 <= score <95:
            total += 3.5
        if 85 <= score < 90:
            total += 3
        if 80 <= score < 85:
            total += 2.5
        if 75 <= score < 80:
            total += 2
        if 70 <= score < 75:
            total += 1.5
        if 65 <= score < 70:
            total += 1
        if 60 <= score < 65:
            total += 0.5
        else:
            total += 0
    print(f"{((int((total/num)*100))/100):.2f}")
main()
