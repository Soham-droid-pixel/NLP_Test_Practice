import nltk
from nltk.corpus import stopwords
import spacy
nltk.download('punkt')
nltk.download('stopwords')

text="This is an example sentence, showing the effect of stopword removal."
#NLTK:
nltk_tokens=nltk.word_tokenize(text)
nltk_stopwords=set(stopwords.words('english'))
nltk_filtered=[word for word in nltk_tokens if word.lower() not in nltk_stopwords]
#Spacy:
nlp=spacy.load('en_core_web_sm')
spacy_filtered=[token.text for token in nlp(text) if not token.is_stop]
print("Original word count",len(text))
print("After NLTK Stopword removal:",nltk_filtered)
print("After Spacy Stopword Removal:",spacy_filtered)
"""Got it 👍 Let’s make this **super revision-friendly** so you can quickly recall for the exam without stress.

---

# 📌 **Stopword Removal – NLTK vs SpaCy (Revision)**

---

## **🔹 NLTK Approach**

**Steps (Memory Trick → `T S F`)**

1. **T** → Tokenize: `nltk.word_tokenize(text)`
2. **S** → Stopwords set: `stopwords.words('english')`
3. **F** → Filter: `[w for w in tokens if w.lower() not in stopwords]`

**Code:**

```python
import nltk
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('stopwords')

tokens = nltk.word_tokenize(text)
stop_set = set(stopwords.words('english'))
filtered_nltk = [w for w in tokens if w.lower() not in stop_set]
```

---

## **🔹 SpaCy Approach**

**Steps (Memory Trick → `N F`)**

1. **N** → NLP pipeline: `nlp = spacy.load(...)`
2. **F** → Filter with `token.is_stop`

**Code:**

```python
import spacy
nlp = spacy.load("en_core_web_sm")

filtered_spacy = [t.text for t in nlp(text) if not t.is_stop]
```

---

# 🧠 **Memory Hack**

Think:

> **“NLTK → Manual Check | SpaCy → Auto Check”**

* NLTK = *you check word in stopwords set*
* SpaCy = *SpaCy checks with `token.is_stop`*

Or remember:

> **“NLTK = 3 Steps (T-S-F) | SpaCy = 2 Steps (N-F)”**

---

# ⚡ **Mini Revision Table**

| Feature         | NLTK                         | SpaCy                    |
| --------------- | ---------------------------- | ------------------------ |
| Tokenization    | `word_tokenize()`            | `nlp(text)`              |
| Stopword Source | `stopwords.words('english')` | Built-in `token.is_stop` |
| Filtering Logic | Manual list comprehension    | Attribute check          |

---

👉 Question: Do you want me to give you a **one-page diagram (flow chart)** that visually shows NLTK vs SpaCy steps side by side (2 arrows each) so it’s stuck in your head? That would be exam gold.
"""