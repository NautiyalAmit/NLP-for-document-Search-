import spacy
from spacy_lookup import Entity

nlp = spacy.load("en")
search = "studied at Berlin"
doc = nlp(search)
search_entity = []
ents = [(e.start_char, e.end_char, e.text) for e in doc.ents]
for i in range(0, len(ents)):
    for j in ents[i]:
        temp = ents[i]
    search_entity.append(temp[2])


entity = Entity(keywords_list=search_entity)
nlp.add_pipe(entity, last=True)

# file_name = "//home//amit//Amit work environment//NLP_for _doc_search//documentsStorage//storageTextFiles//Amit Nautiyal CV nov 2020 1.txt"
# f = open(file_name, "r")
# read_doc = f.read()

read_doc = nlp("amit is studying in  Berlin")

assert doc._.has_entities == True
assert doc[2:5]._.has_entities == True
assert doc[0]._.is_entity == False
assert doc[3]._.is_entity == True
print(read_doc._.entities)
