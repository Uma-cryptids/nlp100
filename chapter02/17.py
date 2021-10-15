with open("popular-names_space.txt") as f:
    s = set()
    for line in f.readlines():
        words = line.split()
        s.add(words[0])
print(len(s))
