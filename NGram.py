import nltk
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
nltk.download('punkt')
nltk.download('punkt_tab')

text="The future of AI is bright and full of opportunities."
tokens=nltk.word_tokenize(text)
unigrams=list(ngrams(tokens,1))
bigrams=list(ngrams(tokens,2))
trigrams=list(ngrams(tokens,3))
print("Unigrams:",unigrams)
print("Biigrams:",bigrams)
print("Trigrams:",trigrams)
