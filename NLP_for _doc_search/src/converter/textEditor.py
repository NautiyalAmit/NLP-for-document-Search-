import re

fin = open(
    "//home//amit//Amit work environment//NLP_for _doc_search//documentsStorage//storageTextFiles//Amit Nautiyal CV nov 2020.txt",
    "rt",
)
fout = open(
    "//home//amit//Amit work environment//NLP_for _doc_search//documentsStorage//storageTextFiles//Amit Nautiyal CV nov 2020 1.txt",
    "wt",
)

for line in fin:
    fout.write(re.sub("\s+", " ", line))

fin.close()
fout.close()
