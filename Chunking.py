import nltk
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

sentence="Donald Trump was born in Queens, New York."
tokens=nltk.word_tokenize(sentence)
pos_taggers=nltk.pos_tag(tokens)

grammar="NP:{<DT>?<JJ>*<NNP>+}"
chunk_parser=nltk.RegexpParser(grammar)
tree=chunk_parser.parse(pos_taggers)
tree.draw()

print("POS tags:",pos_taggers)
print("Chunks:",tree)
"""Tokenize sentence → tokens

Assign POS tags → tags

Define grammar (what kind of phrases to group)

Parse tags into phrases (NP chunks here)

Show output as text or tree

"""
"""Perfect 👍 Let’s create **clear notes** and a **memory-friendly algorithm** so you can recall this anytime.

---

## 📒 **NOTES – NLTK Chunking Process**

---

### **1️⃣ Key Concepts**

* **Chunking** → Grouping words into meaningful phrases (NP = Noun Phrase, VP = Verb Phrase, PP = Prepositional Phrase).
* **POS Tags** are needed before chunking (because chunking patterns are based on word categories).
* **Grammar Rules** are written using regex-like syntax for POS tags.

---

### **2️⃣ Common POS Tags**

| POS Tag      | Meaning                | Example         |
| ------------ | ---------------------- | --------------- |
| DT           | Determiner             | the, a, an      |
| JJ           | Adjective              | big, beautiful  |
| NNP          | Proper noun (singular) | London, Trump   |
| NNS          | Noun plural            | cities, books   |
| VB, VBD, VBN | Verb forms             | eat, was, eaten |
| IN           | Preposition            | in, on, at      |

---

### **3️⃣ Grammar Syntax**

**General format:**

```
LABEL: {<POS_TAG_PATTERN>}
```

Examples:

* `NP: {<DT>?<JJ>*<NNP>+}` → Optional determiner, adjectives, and one or more proper nouns
* `VP: {<VB.*><NP|PP>*}` → Verb followed by noun or prepositional phrases
* `PP: {<IN><NP>}` → Preposition followed by noun phrase

---

### **4️⃣ Steps to Perform Chunking**

1. **Tokenize sentence**
   `nltk.word_tokenize(sentence)`
2. **POS Tagging**
   `nltk.pos_tag(tokens)`
3. **Define Grammar**
   `grammar = "NP: {<DT>?<JJ>*<NNP>+}"`
4. **Create Parser**
   `parser = nltk.RegexpParser(grammar)`
5. **Parse sentence**
   `tree = parser.parse(pos_tags)`
6. **View results**
   `tree.draw()` or `print(tree)`

---

---

## 🧠 **ALGORITHM TO REMEMBER (Memory Trick)**

Think of it as **T P G P P V** = *"The Python Grammar Parses Phrases Visually"*

1️⃣ **T** → Tokenize (`word_tokenize`)
2️⃣ **P** → POS tag (`pos_tag`)
3️⃣ **G** → Grammar (write your chunking rules)
4️⃣ **P** → Parser (RegexpParser with grammar)
5️⃣ **P** → Parse (apply parser to tagged sentence)
6️⃣ **V** → View (tree.draw or print)

---

💡 **Quick Example (NP only)**

```python
tokens = nltk.word_tokenize("Donald Trump was born in New York.")
tags = nltk.pos_tag(tokens)
grammar = "NP: {<DT>?<JJ>*<NNP>+}"
parser = nltk.RegexpParser(grammar)
tree = parser.parse(tags)
tree.draw()
```

---

👉 If you want, I can create a **one-page visual cheat sheet** (with NP, VP, PP grammar + diagram) so you can quickly revise chunking rules before practice.
Do you want that?
"""
# ===== ALGORITHM =====
# 1. Tokenize + POS tag sentence
# 2. Define chunk grammar for NPs (e.g. <DT>?<JJ>*<NNP>+)
# 3. Create RegexpParser
# 4. Parse tags & visualize/print

# ===== EXAM POINTS =====
# * Chunking groups words (e.g. noun phrases)
# * Grammar uses POS tags: DT=det, JJ=adj, NNP=proper noun
# * tree.draw() (optional in lab)
