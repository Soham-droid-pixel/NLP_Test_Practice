import nltk
nltk.download('punkt')
import re,string
text="RT @AI_Expert: The AI conference starts on 10/08/2025!!! #AI #Tech 🚀"
text_lower=text.lower()
cleaned=re.sub(r"@\w+|#\w+|http\S+|[^a-zA-Z\s]"," ",text_lower)
cleaned1=re.sub(r"\s+"," ",cleaned).strip()
print(cleaned1)
print(text_lower)