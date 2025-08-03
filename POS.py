import nltk,spacy
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

text = "John loves eating pizza while Mary reads books in the library."
#NLTK:
tokens=nltk.word_tokenize(text)
nltk_taggers=nltk.pos_tag(tokens)

#Spacy:
nlp=spacy.load('en_core_web_sm')
doc=nlp(text)
spacy_taggers=[(token.text,token.pos_)for token in doc]
print("NLTK taggers:",nltk_taggers)
print("Spacy taggers:",spacy_taggers)