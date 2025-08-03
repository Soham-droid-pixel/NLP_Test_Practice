import nltk
from nltk.stem import PorterStemmer,LancasterStemmer,WordNetLemmatizer
nltk.download('wordnet')
nltk.download('omw-1.4')

words=["running", "flies", "better", "studies", "wolves", "cities"]
lancaster=LancasterStemmer()
porter=PorterStemmer()
wordnet=WordNetLemmatizer()
print("Words:",words)
print("Lancaster words: ",[lancaster.stem(words) for words in words])
print("PorterStemmer words: ",[porter.stem(words) for words in words])
print("Lemmatizer words: ",[wordnet.lemmatize(words) for words in words])

# ===== ALGORITHM =====
# 1. PorterStemmer / LancasterStemmer → stem()
# 2. WordNetLemmatizer → lemmatize()
# 3. Print results & compare

# ===== EXAM POINTS =====
# * Stemming: cuts suffixes (can form non-words)
# * Lemmatization: dictionary-based → correct base word
