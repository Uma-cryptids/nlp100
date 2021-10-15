import gzip
import json

with gzip.open("jawiki-country.json.gz") as f:
    for lines in f:
        line = json.loads(lines)
        if line["title"] == "イギリス":
            with open("British_origin.txt", "w") as o:
                o.writelines(line["text"])
