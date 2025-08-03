from transformers import pipeline
nlp_pipeline=pipeline("token-classification",model="dslim/bert-base-NER")
text="Sundar Pichai became CEO of Google in 2015."
output=nlp_pipeline(text)
for token in output:
    print(token)