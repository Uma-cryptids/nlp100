import sys


def main(fname, n):
    with open(fname) as fin:
        lines = fin.readlines()
        w = len(lines)//n
        for i in range(n):
            with open(fname.replace(".txt", "")+f"{i}.txt", "w") as f:
                if i != n:
                    f.writelines(lines[i:i+w])
                else:
                    f.writelines(lines[i:])


if __name__ == '__main__':
    main(sys.argv[1], int(sys.argv[2]))
