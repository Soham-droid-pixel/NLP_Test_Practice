import spacy
nlp=spacy.load("en_core_web_sm")
sentence="Apple Inc. is planning to open a new office in Mumbai by 2026."
docs=nlp(sentence)
for ent in docs.ents:
    print(f"{ent.text}:{ent.label_}")

# ===== ALGORITHM =====
# 1. Load model: spacy.load("en_core_web_sm")
# 2. Pass text to nlp
# 3. Loop doc.ents → print ent.text, ent.label_

# ===== EXAM POINTS =====
# * ORG=organization, GPE=location, DATE=year/date
# * SpaCy model pre-trained → no training required
