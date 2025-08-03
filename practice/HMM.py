import nltk
from nltk.corpus import brown
from nltk.tag import hmm 
nltk.download("universal_tagset")
text="The quick fox jumps over the lazy dog".split()
train_data=brown.tagged_sents(categories='news',tagset='universal')[:5000]
trainer=hmm.HiddenMarkovModelTrainer()
hmm_tagger=trainer.train_supervised(train_data)

print(hmm_tagger.tag(text))

