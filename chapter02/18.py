with open("popular-names_space.txt") as f,\
        open("sorted.txt", "w") as o:

    lines = sorted([l.split() for l in f.readlines()],
                   key=lambda x: int(x[2]), reverse=True)
    lines = list(map(lambda x: " ".join(x)+"\n", lines))
    o.writelines(lines)
