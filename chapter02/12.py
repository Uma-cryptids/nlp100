with open("popular-names_space.txt") as f,\
        open("col1.txt", "w") as o1,\
        open("col2.txt", "w") as o2:
    for line in f.readlines():
        words = line.split()
        o1.write(words[0]+"\n")
        o2.write(words[1]+"\n")
