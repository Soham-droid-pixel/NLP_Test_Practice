import re;
text="""Contact us at support@example.com or call +91-9876543210. 
Visit our website https://www.mywebsite.org for details. 
Follow us on Twitter @TechGuru and use the hashtag #AI2025. 
Meeting scheduled on 28/07/2025. Beware of badword1 and badword2.
"""
email=re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",text)
phone_numbers=re.findall(r"\+91-\d{10}",text)
urls=re.findall(r"https?://\S+",text)
hashtags=re.findall(r"#\w+",text)
mentions=re.findall(r"@\w+",text)
offensive_words=[word for word in ["badword1","badword2","spamword"]if word in text]
print("Emails",email)
print("Phone numbers:",phone_numbers)
print("URLs:",urls)
print("Hashtags:",hashtags)
print("Mentions:",mentions)
print("Offensive words:",offensive_words)

# ===== ALGORITHM =====
# 1. Import re
# 2. Store text in a variable
# 3. Use re.findall() for:
#    - Email: pattern like user@domain
#    - Phone: +91-XXXXXXXXXX
#    - URL: starts with http/https
#    - Hashtag: starts with #
#    - Mention: starts with @
# 4. Offensive words: loop over bad words list & check if in text
# 5. Print extracted items

# ===== EXAM POINTS =====
# * re.findall(pattern, text) → returns all matches
# * Common patterns:
#   Email: r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
#   Phone (India): r"\+91-\d{10}"
#   URL: r"https?://\S+"
#   Hashtag: r"#\w+"
#   Mention: r"@\w+"
# * Offensive check = simple membership in string


