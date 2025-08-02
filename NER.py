import spacy
nlp=spacy.load("en_core_web_sm")
sentence="Apple Inc. is planning to open a new office in Mumbai by 2026."
docs=nlp(sentence)
for ent in docs.ents:
    print(f"{ent.text}:{ent.label_}")
