import nltk
from nltk.metrics import edit_distance

word1 = "kitten"
word2="sitting"
Edit_Distance=edit_distance(word1,word2)
print(f"Edit distance between{word1} and {word2} is: ",Edit_Distance)

# ===== ALGORITHM =====
# 1. Import edit_distance from nltk.metrics
# 2. Pass word1, word2 → returns min edits (insert/delete/replace)
# 3. Print result

# ===== EXAM POINTS =====
# * Edit Distance measures changes to convert one string to another
# * Example kitten→sitting needs 3 edits
# * Function: edit_distance(str1, str2)
