morph = []
result = []
nouns = ""

with open("neko.txt.mecab") as f:
    for line in f.readlines():
        if "EOS" not in line and line != "\n":
            words = line.split("\t")
            analysys = words[1].split(",")
            morph.append({"surface": words[0],
                          "base": analysys[6],
                          "pos": analysys[0],
                          "pos1": analysys[1]})

for item in morph:
    if item["pos"] == "名詞":
        nouns += item["surface"]
    else:
        if nouns != "":
            result.append(nouns)
        nouns = ""

print(*result[:10], sep="\n")
