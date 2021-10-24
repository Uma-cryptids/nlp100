class Morph:
    def __init__(self, string):
        surface, words = string.split("\t")
        words = words.split(",")
        self.surface = surface
        self.base = words[6]
        self.pos = words[0]
        self.pos1 = words[1]

    def __repr__(self):
        return self.pos


morph = []

with open("ai.ja.txt.parsed") as f:
    for line in f.readlines():
        if "EOS" not in line and line[0] != "*":
            morph.append(Morph(line))
print(*morph[:10], sep="\n")
