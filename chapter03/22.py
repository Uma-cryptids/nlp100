import gzip
import re
import json

pattern = re.compile(r"^.*\[\[Category:(.*?)(?:\|.*)?\]\].*$", re.MULTILINE)

with gzip.open("jawiki-country.json.gz") as f:
    for lines in f.readlines():
        line = json.loads(lines)
        if line["title"] == "イギリス":
            result = pattern.findall(line["text"])
            print(*result, sep="\n")
