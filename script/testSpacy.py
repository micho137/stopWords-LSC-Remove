from script.stopWords import exceptions
import spacy
def preprocess_text(text):
    nlp = spacy.load('es_dep_news_trf')
    doc = nlp(text)
    processed_text = []
    for token in doc:
        print(token.text, token.pos_)
        if token.text not in exceptions:
            if token.pos_ == 'PROPN':
                spell = list(token.text)
                processed_text.extend(spell)
            else:
                if token.pos_ == 'VERB':
                    lemma = token.lemma_
                    processed_text.append(lemma)
                else:
                    textToken = token.text
                    processed_text.append(textToken)
    return processed_text