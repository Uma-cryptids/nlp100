with open("popular-names_space.txt") as f:
    dic = {}
    for line in f.readlines():
        words = line.split()
        if words[0] not in dic.keys():
            dic[words[0]] = 0
        dic[words[0]] += 1
    dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    print(*dic, sep="\n")
