import gzip
import re
import json

pattern1 = re.compile(r"\{\{基礎情報.*\}\}", re.MULTILINE+re.DOTALL)
pattern2 = re.compile(r"^\|(.+?)\s+=\s+(.+?)$",
                      re.MULTILINE)
dic = {}

with gzip.open("jawiki-country.json.gz") as f:
    for lines in f.readlines():
        line = json.loads(lines)
        if line["title"] == "イギリス":
            result = pattern1.findall(line["text"])
            result = pattern2.findall("".join(result))
            for name, text in result:
                print(text)
                dic[name] = text
print(dic)
