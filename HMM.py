import nltk
from nltk.corpus import brown
from nltk.tag import hmm
nltk.download('brown')
nltk.download('universal_tagset')
sentence="The quick brown fox jumps over the lazy dog."
training_data=brown.tagged_sents(categories="news",tagset='universal')[:5000000]
trainer=hmm.HiddenMarkovModelTrainer()
hmm_tagger=trainer.train_supervised(training_data)
print("HMM tags are:",hmm_tagger.tag(sentence.split()))

# ==================== HMM POS TAGGER SUMMARY ====================
# 1. Use Brown Corpus (POS-tagged data)
#    → brown.tagged_sents(categories='news', tagset='universal')
# 2. Limit to [:500] sentences for small training
# 3. Create Trainer: hmm.HiddenMarkovModelTrainer()
# 4. Train Model: trainer.train_supervised(train_data)
# 5. Tag New Sentence: hmm_tagger.tag(sentence.split())
#
# Logic:
# HMM learns probability of tags from old data → predicts tags for new words
#
# Memory Trick (C-T-T-T):
# C = Corpus
# T = Train Data
# T = Trainer
# T = Test on new sentence
#
# Example Output:
# [('The', 'DET'), ('quick', 'ADJ'), ('brown', 'ADJ'), ('fox', 'NOUN')]
#
# Use Cases:
# ✅ Statistical POS tagging
# ✅ Works well with enough training data
# ================================================================

# ===== ALGORITHM =====
# 1. Load Brown corpus tagged_sents
# 2. Train with HiddenMarkovModelTrainer
# 3. Tag new sentence

# ===== EXAM POINTS =====
# * HMM learns tag probabilities
# * Small training = lower accuracy
