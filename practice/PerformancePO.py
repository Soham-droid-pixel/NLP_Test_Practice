import nltk,spacy
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

gold = [('The', 'DT'), ('dog', 'NN'), ('chased', 'VBD'), ('the', 'DT'), ('cat', 'NN')]
text = "The dog chased the cat."

# NLTK
tokens = nltk.word_tokenize(text)
nltk_tags = nltk.pos_tag(tokens)

# SpaCy
nlp=spacy.load('en_core_web_sm')
doc = nlp(text)
spacy_tags = [(token.text, token.tag_) for token in doc]

# Accuracy function
def compute_accuracy(pred, gold):
    correct = sum(1 for p, g in zip(pred, gold) if p[1] == g[1])
    return correct / len(gold)

print("NLTK Accuracy:", compute_accuracy(nltk_tags, gold))
print("SpaCy Accuracy:", compute_accuracy(spacy_tags, gold))
