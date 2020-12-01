import io

import spacy
from spacy.lang.en import English
from spacy.matcher import Matcher
from textacy.spacier import utils as spacy_utils

"""
create the nlp object
"""


def create_nlp_object():
    nlp = spacy.load("en_core_web_sm")
    matcher = Matcher(nlp.vocab)
    return nlp


nlp = create_nlp_object()
"""
load the text file
"""
file_name = "//home//amit//Amit work environment//NLP_for _doc_search//documentsStorage//storageTextFiles//resume_.txt"
f = open(file_name, "r")
read_doc = f.read()
# print(nlp(read_doc))


doc = nlp(read_doc)
document_entity = []
ents = [(e.start_char, e.end_char, e.text) for e in doc.ents]
for i in range(0, len(ents)):
    for j in ents[i]:
        temp = ents[i]
    document_entity.append(temp[2])
    # print(temp[2])


"""
    Generates a few simple answer  filling pieces from sentences
"""


def answer_generator(text):
    doc = nlp(text)
    results = []
    for sentence in doc.sents:
        root = sentence.root
        results.append(root)
        break

        """
        TODO: below code not needed as of now but is required for complicated ops.
        """
        # ask_about = spacy_utils.get_subjects_of_verb(root)
        # answers = spacy_utils.get_objects_of_verb(root)
        # main_verb = spacy_utils.get_main_verbs_of_sent(sentence)
        # if len(ask_about) > 0 and len(answers) > 0:
        #     results.append({"ask": ask_about, "answers": answers})
        # print(results)
    return results


"""
search string 
"""

search = input("enter the search query:")
print("you searched for :{}".format(search))

"""
sample search queries:
"""
# search = "which student studied at Technical University Berlin and Germany "
# search="which student studied in Germany "
Search_doc = nlp(search)
search_entity = []
ents = [(e.start_char, e.end_char, e.text) for e in Search_doc.ents]
for i in range(0, len(ents)):
    for j in ents[i]:
        temp = ents[i]
    # print(temp[2])
    search_entity.append(temp[2])


"""
generate the output 

"""


def output():
    for i in range(0, len(search_entity)):
        if search_entity[i] in document_entity:
            print(generator)
        else:
            print("null")


example_text = read_doc
doc = nlp(example_text)
generator = answer_generator(example_text)
output()

