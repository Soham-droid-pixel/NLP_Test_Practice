import nltk,spacy
nltk.download("averaged_perceptron_model")
nltk.download("punkt")

text="John loves eating pizza while Mary reads books in the library."
#NLTK:
tokens=nltk.word_tokenize(text)
nltk_taggers=nltk.pos_tag(tokens)
#Spacy:
nlp=spacy.load("en_core_web_sm")
doc=nlp(text)
spacy_taggers=[(token.text,token.tag_) for token in doc]

print("NLTK:",nltk_taggers)
print("Spacy:",spacy_taggers)