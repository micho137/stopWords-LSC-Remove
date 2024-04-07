import spacy

def preprocess_text(text):
    # Aqui cargamos el modelo spañol de Spacy
    nlp = spacy.load('es_core_news_sm')

    # Se definen los STOP WORDS excluyendo los prononmbres y terminos a utilizar 
    stop_words = set(['además', 'ante', 'bajo', 'se', 'me', 'cabe', 'contra', 'cuando', 'de', 'desde', 'donde', 'durante',
                      'e', 'a', 'el', 'en', 'entre', 'hacia', 'la', 'las', 'lo', 'los', 'mis',
                      'por', 'qué', 'según', 'sobre', 'tras', 'un', 'una'])

    # POS tags permitidos (Pronombres, Verbos, Adjetivos)
    allowed_tags = ['PRON', 'VERB', 'ADJ']

    # Procesar el texto con Spacy
    doc = nlp(text)

    processed_text = []

    # Iterar los tokens en el texto procesado
    for token in doc:
        # Verificar si el token no es una STOP WORD (excluyendo los pronombres) y si el POS tag se encuentra en los tags permitidos
        if token.text.lower() not in stop_words or token.pos_ in allowed_tags:
            # Lemmatize the token
            lemma = token.lemma_
            processed_text.append(lemma)

    return processed_text

# Ejemplo
# text = "Karlos quiere comprar un sueter"
# processed_text = preprocess_text(text)
# print(processed_text)
