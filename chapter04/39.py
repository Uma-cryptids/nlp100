import matplotlib.pyplot as plt

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

result = sorted(result.items(), key=lambda x: x[1], reverse=True)

x = list(range(1, len(result)+1))
y = [i[1] for i in result]

plt.rcParams['font.family'] = "Hiragino sans"
plt.scatter(x, y, s=10)
plt.title("Zeppの法則")
plt.xlabel("出現頻度")
plt.ylabel("出現頻度順位")
plt.xscale("log")
plt.yscale("log")
plt.show()
