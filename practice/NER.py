import nltk,spacy
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

text="Tesla plans to launch a new Gigafactory in Berlin by 2026."
token=nltk.word_tokenize(text)
nlp_tagger=nltk.pos_tag(token)

nlp=spacy.load("en_core_web_sm")
doc=nlp(text)
for ents in doc.ents:
    print(ents.text,ents.label_)