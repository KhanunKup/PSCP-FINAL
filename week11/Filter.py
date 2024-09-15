"""Filter"""
import json
def main(dic,fil):
    """main"""
    result = []
    dic = json.loads(dic)
    sorted_dic = sorted(dic.items())
    for i in sorted_dic:
        if i[-1] >= fil:
            result.append(i)
    if not result:
        print("Nope")
    for i in result:
        print(f"{i[0]}\t{i[-1]:.2f}")
main(input(),float(input()))
