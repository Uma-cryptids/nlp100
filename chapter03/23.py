import gzip
import re
import json

pattern = re.compile(r"={2,}.*={2,}")

with gzip.open("jawiki-country.json.gz") as f:
    for lines in f.readlines():
        line = json.loads(lines)
        if line["title"] == "イギリス":
            result = pattern.findall(line["text"])
            for item in result:
                print("level:", item.count("=")//2, "\t",
                      item.replace("=", "").replace(" ", ""))
