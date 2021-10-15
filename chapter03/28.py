import gzip
import re
import json


def remove_markup(txt):
    markup1 = re.compile(r"\'{2,}")
    markup2 = re.compile(r"\[\[(.+?)\]\]")
    markup3 = re.compile(r"<.*>")
    markup4 = re.compile(r"\{\{(?:仮リンク\|)*(?:lang\|.*\|)*(.+?)\}\}")
    markup5 = re.compile(r"ファイル:(.*?)(?:\|.+)")

    txt = re.sub(markup1, "", txt)
    txt = re.sub(markup2, "\\1", txt)
    txt = re.sub(markup3, "", txt)
    txt = re.sub(markup4, "\\1", txt)
    txt = re.sub(markup5, "\\1", txt)
    return txt


pattern1 = re.compile(r"^\{\{基礎情報.*?^\}\}", re.MULTILINE+re.DOTALL)
pattern2 = re.compile(r'^\|(.+?)\s*=\s*(.+?)$',
                      re.MULTILINE+re.DOTALL)
dic = {}

with gzip.open("jawiki-country.json.gz") as f:
    for lines in f.readlines():
        line = json.loads(lines)
        if line["title"] == "イギリス":
            result = pattern1.findall(line["text"])
            result = pattern2.findall("".join(result))
            for name, text in result:
                dic[name] = remove_markup(text)

