s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
print([*map(len, s.replace(",", "").replace(".", "").split())])