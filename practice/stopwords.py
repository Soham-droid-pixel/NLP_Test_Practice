import nltk,spacy
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')
text="Natural Language Processing is an exciting field in Artificial Intelligence."
#nltk:
token=nltk.word_tokenize(text)
nltk_stopwords=set(stopwords.words('english'))
nltk_filtered=[word for word in token if word.lower() not in nltk_stopwords]
#spacy:
nlp=spacy.load("en_core_web_sm")
spacy_filtered=[token.text for token in nlp(text) if not token.is_stop]
print("Original Word Count:", len(token))
print("After NLTK Stopword Removal:", nltk_filtered)
print("After SpaCy Stopword Removal:", spacy_filtered)
