import matplotlib.pyplot as plt
import numpy as np

morph = []
lines = [[]]
result = {}
idx = 0

with open("neko.txt.mecab") as f:
    for line in f.readlines():
        if "EOS" not in line and line != "\n" and line != "*\n":
            words = line.split("\t")
            analysys = words[1].split(",")
            morph.append({"surface": words[0],
                          "base": analysys[6],
                          "pos": analysys[0],
                          "pos1": analysys[1]})

for item in morph:
    if item["surface"] != "。":
        lines[idx].append(item)
    else:
        lines[idx].append(item)
        lines.append([])
        idx += 1

for line in lines:
    for item in line:
        if item["base"] == "猫":
            for target in line:
                if target["pos"] != "記号" and target["base"] != "猫":
                    if target["base"] not in result.keys():
                        result[target["base"]] = 0
                    result[target["base"]] += 1
            break

result = sorted(result.items(), key=lambda x: x[1], reverse=True)

#表示数
NUM = 20
left = np.arange(NUM)
height = np.array(list(map(lambda x: x[1], result[:NUM])))
label = list(map(lambda x: x[0], result[:NUM]))
plt.rcParams['font.family'] = "Hiragino sans"


plt.bar(left, height, tick_label=label)
plt.title("単語出現回数")
plt.xlabel("単語")
plt.ylabel("出現回数")
plt.show()
