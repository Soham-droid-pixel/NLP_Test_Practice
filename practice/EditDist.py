import nltk
from nltk import edit_distance
nltk.download('punkt')
word1="flaw"
word2="lawn"
operations=edit_distance(word1,word2)
print(operations)