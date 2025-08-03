import nltk, spacy
from transformers import BertTokenizer

nltk.download('punkt')
nlp = spacy.load("en_core_web_sm")

text = "Artificial Intelligence is revolutionizing the world."

# Word-level tokenization
nltk_tokens = nltk.word_tokenize(text)
spacy_tokens = [token.text for token in nlp(text)]

# Character-level tokenization
char_tokens = list(text)

# Subword tokenization (WordPiece - BERT)
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
subword_tokens = tokenizer.tokenize(text)

print("NLTK Word Tokens:", nltk_tokens)
print("SpaCy Word Tokens:", spacy_tokens)
print("Character Tokens:", char_tokens[:20])  # first 20 chars
print("Subword Tokens (WordPiece):", subword_tokens)
