def ngram(n, s):
    return list(zip(*[s[i:]for i in range(n)]))


X = set(ngram(2, "paraparaparadise"))
Y = set(ngram(2, "paragraph"))

# 和集合
print(X | Y)
# 積集合
print(X & Y)
# 差集合
print(X - Y)
# se in X
print(("s", "e") in X)
# se in Y
print(("s", "e") in Y)