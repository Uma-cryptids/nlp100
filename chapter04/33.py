morph = []
result = []

with open("neko.txt.mecab") as f:
    for line in f.readlines():
        if "EOS" not in line and line != "\n":
            words = line.split("\t")
            analysys = words[1].split(",")
            morph.append({"surface": words[0],
                          "base": analysys[6],
                          "pos": analysys[0],
                          "pos1": analysys[1]})


for i in range(1, len(morph)-1):
    if morph[i]["surface"] == "の" or morph[i]["pos"] == "助詞":
        if morph[i-1]["pos"] == "名詞" and morph[i+1]["pos"] == "名詞":
            result.append(morph[i-1]["surface"] + "の" + morph[i+1]["surface"])
