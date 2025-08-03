import nltk,spacy
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
gold = [('The', 'DT'), ('dog', 'NN'), ('chased', 'VBD'), ('the', 'DT'), ('cat', 'NN')]
text = "The dog chased the cat."
#nltk:
tokens=nltk.word_tokenize(text)
nltk_taggers=nltk.pos_tag(tokens)
#spacy:
nlp=spacy.load('en_core_web_sm')
doc=nlp(text)
spacy_taggers=[(token.text,token.tag_) for token in doc]

def accuracy(pred,gold):
    correct=sum( 1 for p,g in zip(pred,gold) if p[1]==g[1])
    return correct/len(gold)

print("NLTK accuarcy: ",accuracy(nltk_taggers,gold))
print("Spacy accuracy: ",accuracy(spacy_taggers,gold))
"""zip(pred, gold)

Pairs predicted tags with gold standard tags.p[1] == g[1]

p[1] is the predicted tag (POS tag from model).

g[1] is the correct tag (POS tag from gold standard).

This checks if prediction matches the gold tag.

Returns True if correct, False if wrong.

sum(p[1] == g[1] for p, g in zip(...))

In Python, True = 1 and False = 0.

So summing gives number of correct predictions.

/ len(gold)

Divides correct predictions by total predictions.

Gives accuracy as a fraction (e.g., 1.0 = 100% correct)."""