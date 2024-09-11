"""Runner"""
def find_whosfastest(goal,vec,start,i):
    """calculation"""
    result = (goal - (start))/(vec)
    return result,-vec,i #return -vec for sorting
def main():
    """main"""
    vec = []
    start_point = []
    fastest_runner = []
    goal = float(input())
    runner = int(input())
    for _ in range(runner): # create a list of velocity and strating point
        data = input().split()
        vec.append(float(data[0]))
        start_point.append(float(data[-1]))
    for i in range(runner):
        fastest_runner.append(find_whosfastest(goal, vec[i], start_point[i],i + 1))
        # i for sort number of runner
    fastest_runner.sort()
    print(fastest_runner[0][-1])
main()
