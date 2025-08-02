import nltk
from nltk.metrics import edit_distance

word1 = "kitten"
word2="sitting"
Edit_Distance=edit_distance(word1,word2)
print(f"Edit distance between{word1} and {word2} is: ",Edit_Distance)

