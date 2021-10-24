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


if __name__ == '__main__':
    with open("ai.ja.txt.parsed") as f:
        sentence = []
        sentences = []
        for file_line in f.readlines():
            if "EOS" in file_line:
                sentences.append(Sentence(sentence))
                sentence = []
            else:
                sentence.append(file_line)

    with open("ai.ja.txt.casewphrase", "w") as f:
        copas = {}
        for sentence in sentences:
            for chunk in sentence.chunks:
                if chunk.srcs != -1:
                    a = chunk
                    b = sentence.chunks[chunk.srcs]
                    c = ""
                    if any(map(lambda x: x.pos == "名詞", a.morphs)):
                        if any(map(lambda x: x.pos == "動詞", b.morphs)):
                            for morph in b.morphs:
                                if morph.pos == "動詞":
                                    c = morph.base
                                    break
                            if c not in copas.keys():
                                copas[c] = []
                            copas[c].append(a)
        for varb, nouns in copas.items():
            if nouns is not None:
                result = {}
                cases = []
                phrases = []
                for noun in nouns:
                    for morph in noun.morphs:
                        if morph.pos1 == "格助詞":
                            if morph.base not in result.keys():
                                result[morph.base] = []
                            result[morph.base].append(str(noun))
                if result != {}:
                    f.write(f"{varb}\t")
                    result = sorted(result.items(), key=lambda x: x[0])
                    for case, phrase in result:
                        cases.append(case)
                        phrases.append(" ".join(phrase))
                    f.write(" ".join(cases))
                    f.write("\t")
                    f.write(" ".join(phrases))
                    f.write("\n")
