import nltk
from nltk import RegexpTagger
patterns = [
    (r'.*ing$', 'VBG'),        # gerunds
    (r'.*ed$', 'VBD'),         # past tense verbs
    (r'.*es$', 'VBZ'),         # 3rd person singular verbs
    (r'^Ravi$', 'NNP'),        # proper noun
    (r'cricket|TV', 'NN'),     # nouns
    (r'the|and|a|daily', 'DT'),# determiners/conjunctions
    (r'.*', 'NN')              # default noun
]
sentence="Ravi plays cricket and watches TV daily."
tagger=RegexpTagger(patterns)
tokens=nltk.word_tokenize(sentence)
Rule_based=tagger.tag(tokens)
print("Rule Based taggers: ",Rule_based)