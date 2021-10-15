import sys


def main(fname, n):
    with open(fname) as f:
        for _ in range(n):
            print(f.readline(), end="")


if __name__ == '__main__':
    main(sys.argv[1], int(sys.argv[2]))
