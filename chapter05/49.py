import CaboCha


class Morph:
    def __init__(self, in_line):
        surface, words = in_line.split("\t")
        words = words.split(",")
        self.surface = surface
        self.base = words[6]
        self.pos = words[0]
        self.pos1 = words[1]

    def __repr__(self):
        return self.surface

    def __str__(self):
        return self.surface


class Chunk:
    def __init__(self, morphs, dst, srcs):
        self.morphs = morphs
        self.dst = dst
        self.srcs = srcs

    @classmethod
    def parse_lines(cls, in_lines):
        __idx_line = in_lines[0].split()
        __morph = []
        __dst = int(__idx_line[1])
        srcs = int(__idx_line[2][:-1])
        for __line in in_lines[1:]:
            if not any(map(__line.__contains__, ("記号", "カッコ"))):
                __morph.append(Morph(__line))
        return Chunk(__morph, __dst, srcs)

    def __repr__(self):
        return "".join(str(morph) for morph in self.morphs)

    def __str__(self):
        return "".join(str(morph) for morph in self.morphs)


class Sentence:
    def __init__(self, in_sentence):
        self.chunks = []

        __chunk_lines = []
        for __line in in_sentence:
            if __line != "":
                if __line[0] == "*":
                    if __chunk_lines != []:
                        self.chunks.append(Chunk.parse_lines(__chunk_lines))
                    __chunk_lines = [__line]
                else:
                    __chunk_lines.append(__line)
        if __chunk_lines != []:
            self.chunks.append(Chunk.parse_lines(__chunk_lines))

    def __repr__(self):
        return "".join(str(item) for item in self.chunks)


def replace(in_chunk, word):
    rtn = ""
    flag = True
    for morph in in_chunk.morphs:
        if morph.pos == "名詞":
            if flag:
                rtn += word
                flag = False
        else:
            rtn += morph.surface
    return rtn


if __name__ == '__main__':
    input_sentence = "ジョン・マッカーシーはAIに関する最初の会議で人工知能という用語を作り出した。"
    cp = CaboCha.Parser()
    parse = cp.parse(input_sentence)
    parsed = parse.toString(CaboCha.FORMAT_LATTICE)
    sentences = []
    sentence = []

    for line in parsed.split("\n"):
        if "EOS" in line:
            sentences.append(Sentence(sentence))
            sentence = []
        else:
            sentence.append(line)

    with open("ai.ja.txt.pass", "w") as f:
        for sentence in sentences:
            all_path = []
            for chunk in sentence.chunks:
                if any(map(lambda x: x.pos == "名詞", chunk.morphs)):
                    now = chunk
                    path = [chunk]
                    while now.srcs != -1:
                        now = sentence.chunks[now.srcs]
                        path.append(now)
                    all_path.append(path)
            for i in range(len(all_path)):
                path1 = all_path[i][:-1]
                varb = str(all_path[i][-1])
                for j in range(i, len(all_path)):
                    path2 = all_path[j][:-1]
                    if not any(map(path1.__contains__, path2)) and len(path1) > 0 and len(path2) > 0:
                        s1 = replace(path1[0], "X")
                        s2 = replace(path2[0], "Y")
                        if len(path1) >= 2:
                            s1 += " -> " + \
                                " -> ".join(str(x) for x in path1[1:])
                        if len(path2) >= 2:
                            s2 += " -> " + \
                                " -> ".join(str(x) for x in path2[1:])
                        f.write(f"{s1} | {s2} | {varb}\n")

                if len(path1) >= 2:
                    for j in range(1, len(path1)):
                        f.write("{} -> {}\n".format(
                                replace(path1[0], "X"), replace(path1[j], "Y")))
