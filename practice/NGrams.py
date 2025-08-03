import nltk
from nltk.util import ngrams
nltk.download("punkt")

text="Machine Learning models are improving rapidly"
token=nltk.word_tokenize(text)
unigrams=list(ngrams(token,1))
bigrams=list(ngrams(token,2))
trigrams=list(ngrams(token,3))
print(unigrams)
print(bigrams)
print(trigrams)