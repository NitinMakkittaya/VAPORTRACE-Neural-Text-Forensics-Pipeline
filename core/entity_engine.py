import spacy

# Load the NLP model for Named Entity Recognition
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    print("WARNING: SpaCy model not found. Run: python -m spacy download en_core_web_sm")
    nlp = None

def detect_entity_tampering(orig_text, mod_text):
    if not nlp:
        return []
    
    doc1 = nlp(orig_text)
    doc2 = nlp(mod_text)
    
    ents1 = {ent.text for ent in doc1.ents if ent.label_ in ['MONEY', 'DATE', 'ORG', 'PERSON']}
    ents2 = {ent.text for ent in doc2.ents if ent.label_ in ['MONEY', 'DATE', 'ORG', 'PERSON']}
    
    # Find entities in modified text that weren't in the original
    tampered = ents2 - ents1
    return list(tampered)