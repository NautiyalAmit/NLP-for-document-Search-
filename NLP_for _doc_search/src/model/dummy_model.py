import io

import spacy
from spacy.lang.en import English
from spacy.matcher import Matcher
from textacy.spacier import utils as spacy_utils

# ## getting the current path
# cur_dir = os.getcwd()
# # navigating to the data folder
# data_path = os.path.join(cur_dir, "data")

# # Iterating the contents of the folder
# for root, sub_dir,files in os.walk(data_path):
#     ## only reading the first file
#     for i,f in enumerate(files[0:1]):
#         file_path = os.path.join(data_path,f)
#         print ("processing file no :", i+1,'\n')
#         text = open(file_path,'r').read()
#         ## Printing a sample text file
#         print (text)

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

file_name = "//home//amit//Amit work environment//NLP_for _doc_search//documentsStorage//storageTextFiles//Amit Nautiyal CV nov 2020 1.txt"
f = open(file_name, "r")
read_doc = f.read()
# print(nlp(read_doc))

"""
search string 
"""
search = "what are documents issued by pavan-kumar ?"
search_doc = nlp(search)
for token in search_doc:
    # Get the token text, part-of-speech tag and dependency label
    token_text = token.text
    token_pos = token.pos_

    # This is for formatting only
    print(f"{token_text:<12}{token_pos:<10}")


"""
look in the file for the searched string
"""
doc = nlp(read_doc)
"""
understand these relationship as a parent-child format as well,
looking at one word at a time

lets explain this above relationship
"""
for token in doc:
    print(
        f"token: {token.text},\t dep: {token.dep_},\t head: {token.head.text},\t pos: {token.head.pos_},\
    ,\t children: {[child for child in token.children]}"
    )

"""
to generate the question consiedering the subject and obj of the verb 
"""


def question_genrator(eg_text):
    """
    Generates a few simple questions  filling pieces from sentences
    """
    doc = nlp(eg_text)
    results = []
    for sentence in doc.sents:
        root = sentence.root
        ask_about = spacy_utils.get_subjects_of_verb(root)
        answers = spacy_utils.get_objects_of_verb(root)
        if len(ask_about) > 0 and len(answers) > 0:
            if root.lemma_ == "be":
                question = f"What {root} {ask_about[0]}?"
            else:
                question = f"What does {ask_about[0]} {root.lemma_}?"
            results.append({"question": question, "answers": answers})
    return results


example_text = read_doc
doc = nlp(example_text)
print(question_genrator(example_text))
