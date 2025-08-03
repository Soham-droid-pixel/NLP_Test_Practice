import re
import string
sentence="RT @user123!!! The PRICE of Bitcoin hit $30,000 today!!! #Crypto 🚀🚀"
text_lower=sentence.lower()
cleaned_sen=re.sub(r"@\w+|#\w+|http\S+|[^a-zA-Z\s]"," ",text_lower)
cleaned=re.sub(r"\s+"," ",cleaned_sen).strip()
print("Cleaned sentence:",cleaned)
print("Sentence:",sentence)

# ===== ALGORITHM =====
# 1. Lowercase
# 2. Remove mentions/hashtags/special chars with regex
# 3. Remove extra spaces
# 4. Print cleaned text

# ===== EXAM POINTS =====
# * Common regex: r"@\w+|#\w+|http\S+|[^a-zA-Z\s]"
# * Always strip() after cleaning
