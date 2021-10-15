def cipher(s):
    return "".join(chr(219 - ord(c)) if c.islower() else c for c in s)

print("supercolorpixelisticxdridocious")
print(cipher("supercolorpixelisticxdridocious"))
print(cipher(cipher("supercolorpixelisticxdridocious")))