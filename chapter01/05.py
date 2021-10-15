def ngram(n, s):
    return list(zip(*[s[i:]for i in range(n)]))

#単語 bi-gram
print(*ngram(2, "I am an NLPer".split()))
#文字 bi-gram
print(*ngram(2, "I am an NLPer"))