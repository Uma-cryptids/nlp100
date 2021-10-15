with open("col1.txt") as f, open("col2.txt") as g:
    with open("marge.txt", "w") as o:
        for n, s in zip(f.readlines(), g.readlines()):
            o.write(n[:-1]+" "+s)
