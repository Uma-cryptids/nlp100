with open("popular-names.txt") as f:
    with open("popular-names_space.txt","a") as out:
        s = list(map(lambda x: x.replace("\t", " "), f.readlines()))
        out.writelines(s)
        