s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
s, d = s.replace(",", "").replace(".", "").split(), {}
for i in range(len(s)):
    if i in [0, 4, 5, 6, 7, 8, 14, 15, 18]:
        d[s[i][0]] = i + 1
    else:
        d[s[i][:2]] = i + 1
print(d)
