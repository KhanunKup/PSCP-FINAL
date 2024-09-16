"""Imposter"""
import json
def main():
    """main"""
    member = {}
    vote_out = {}
    count = 0
    while True:
        data = input()
        if data == "Start":
            break
        member.update(json.loads(data))
    while True: # remove who's eliminate
        data = input()
        if data == "End":
            break
        vote_out.update({data:member[data]})
        member.pop(data)
    for i in member.values(): #count imposter
        if i == "Impostor":
            count += 1
    sorted_mem = dict(sorted(member.items()))
    vote_out = dict(sorted(vote_out.items()))
    print(f"{count} Impostor Remains\n***Alive***")
    for key,value in sorted_mem.items():
        print(f"{key} : {value}")
    print("***Dead***")
    for key,value in vote_out.items():
        print(f"{key} : {value}")
main()
