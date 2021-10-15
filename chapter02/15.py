import sys


def main(fname, n):
    with open(fname) as f:
        lines = f.readlines()
        for line in lines[len(lines)-n:]:
            print(line, end="")


if __name__ == '__main__':
    main(sys.argv[1], int(sys.argv[2]))
