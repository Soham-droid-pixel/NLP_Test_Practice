import re
import string

text = """Email: info@company.com  
Phone: +91-9988776655  
Website: https://www.example.org  
Twitter: @AI_Lab  
Hashtag: #NLP2025  
"""

# Regex patterns
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
phones = re.findall(r"\+91-\d{10}", text)
urls = re.findall(r"https?://\S+", text)
mentions = re.findall(r"@\w+", text)
hashtags = re.findall(r"#\w+", text)

print("Emails:", emails)
print("Phones:", phones)
print("URLs:", urls)
print("Mentions:", mentions)
print("Hashtags:", hashtags)
