import matplotlib.pyplot as plt
import numpy as np

morph = []
result = {}

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
    if item["pos"] != "記号":
        if item["base"] not in result.keys():
            result[item["base"]] = 0
        result[item["base"]] += 1

result = np.array(list(result.values()))

plt.rcParams['font.family'] = "Hiragino sans"

plt.hist(result, log=True, bins=50)
plt.title("単語出現頻度")
plt.xlabel("頻度")
plt.ylabel("単語数")
plt.show()
