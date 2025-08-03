import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

text="Barack Obama was born in Honolulu, Hawaii, and served as the 44th President of the United States."
tokens=nltk.word_tokenize(text)
nltk_taggers=nltk.pos_tag(tokens)

grammar="NP:{<DT>?<JJ>*<NNP>+}"
chunk_parser=nltk.RegexpParser(grammar)
chunking=chunk_parser.parse(nltk_taggers)
chunking.draw()
print("Chunking: ",chunking)