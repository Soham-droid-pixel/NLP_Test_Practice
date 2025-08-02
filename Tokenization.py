import nltk,spacy
from transformers import BertTokenizer
nlp=spacy.load("en_core_web_sm")
nltk.download('punkt')
text="Artificial Intelligence is revolutionizing the world."
nltk_tokens=nltk.word_tokenize(text)
spacy_tokens=[token.text for token in nlp(text)]
char_tokens=list(text)
tokenizer=BertTokenizer.from_pretrained("bert-base-uncased")
subword_tokens=tokenizer.tokenize(text)
print("NLTK tokens:",nltk_tokens)
print("Spacy tokens:",spacy_tokens)
print("Sub-word Tokens:",subword_tokens)
print("Character level tokens:",char_tokens)
"""Got it 👍 You want a **memory hack** so you can recall how to write this code during your exam.

I’ll give you:

* **Core idea breakdown**
* **Memory-friendly algorithm** (step order + keywords)
* **Mini template** you can rewrite in seconds

---

## **📌 Core Idea**

You are simply **tokenizing the same text in 4 ways**:

1. **NLTK** → word-level
2. **SpaCy** → word-level with NLP pipeline
3. **Python list** → character-level
4. **BERT** → subword-level

---

## **🧠 Memory Algorithm (Exam Shortcut)**

Think: **“N S C B → 4 Tokenizers”**

* **N** → NLTK → `word_tokenize`
* **S** → SpaCy → `token.text for token in nlp(text)`
* **C** → Characters → `list(text)`
* **B** → BERT → `BertTokenizer.from_pretrained(...).tokenize(text)`

---

## **⚡ Exam-Ready Template (Bare Minimum to Remember)**

You can memorize just this skeleton:

```python
import nltk, spacy
from transformers import BertTokenizer

# Load models
nltk.download('punkt')
nlp = spacy.load("en_core_web_sm")
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

text = "Your text here"

# Tokenizations
nltk_tokens = nltk.word_tokenize(text)
spacy_tokens = [t.text for t in nlp(text)]
char_tokens = list(text)
bert_tokens = tokenizer.tokenize(text)

# Print
print(nltk_tokens)
print(spacy_tokens)
print(char_tokens)
print(bert_tokens)
```

---

## **💡 How to Remember in Exam**

* **Think order:** `NLTK → SpaCy → Char → BERT`
* **Key methods to remember:**

  * `nltk.word_tokenize(text)`
  * `nlp(text)`
  * `list(text)`
  * `tokenizer.tokenize(text)`

---

👉 If you want, I can also make you a **one-page visual “Tokenization Cheat Sheet”** with a small diagram (NLTK → SpaCy → Char → BERT) so you can revise just before exam without reading code.
Do you want that?
"""