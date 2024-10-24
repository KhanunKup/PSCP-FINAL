dic = {}
text = input()
for i in text:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
print(" ".join(dic))