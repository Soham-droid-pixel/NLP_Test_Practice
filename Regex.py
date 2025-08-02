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


