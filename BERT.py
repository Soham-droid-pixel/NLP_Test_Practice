from transformers import pipeline
nlp_pipeline=pipeline("token-classification",model="dslim/bert-base-NER",aggregation_strategy='simple')
text="Elon Musk founded SpaceX in 2002."
output=nlp_pipeline(text)
for item in output:
    print(item)

# ==================== BERT NER SUMMARY ====================
# 1. Use Hugging Face pipeline for NER
#    pipeline("token-classification", model="dslim/bert-base-NER")
# 2. Pass text → model returns entities
# 3. Output shows word, entity type (PER, ORG, DATE), and confidence
# 4. B-PER = Beginning of Person, I-PER = Inside Person
#    ORG = Organization, DATE = Date
# 5. Pretrained model → No training needed
# ==========================================================

# ===== ALGORITHM =====
# 1. Use pipeline("token-classification", model="dslim/bert-base-NER")
# 2. Pass text
# 3. Loop output → print word, entity, score

# ===== EXAM POINTS =====
# * B-PER/I-PER = person, ORG=organization, DATE=date
# * Transformer models = pretrained, no training required
