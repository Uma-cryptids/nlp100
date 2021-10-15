from random import sample


def typo(s):
    # sample(w[1:-2],len(w)-2)
    return [w[0]+"".join(sample(w[1:-1], len(w)-2))+w[-1] if len(w) > 4 else w for w in s]


print(*typo("I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind .".split()))
