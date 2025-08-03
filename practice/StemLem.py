import nltk
from nltk import LancasterStemmer,PorterStemmer,WordNetLemmatizer
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('omw-1.4')

text=["running", "flies", "better", "wolves", "cities"]

LancasterStemmer_words=LancasterStemmer()
PorterStemmer_words=PorterStemmer()
WordNetLemmatizer_words=WordNetLemmatizer()

print("LS:",[LancasterStemmer_words.stem(word) for word in text])
print("PS:",[PorterStemmer_words.stem(word) for word in text])
print("WNL:",[WordNetLemmatizer_words.lemmatize(word) for word in text])
