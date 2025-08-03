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

# ===== ALGORITHM =====
# 1. Import nltk, download punkt
# 2. Tokenize text
# 3. Generate ngrams(tokens, n) for n=1,2,3
# 4. Print unigrams, bigrams, trigrams

# ===== EXAM POINTS =====
# * Unigram = single words
# * Bigram = word pairs → adds some context
# * Trigram = word triplets → better context
# * ngrams from nltk.util

