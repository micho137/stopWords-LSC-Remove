""" import spacy
from spacy.lang.es.stop_words import STOP_WORDS

def obtener_palabras_clave(oracion):
    nlp = spacy.load('es_core_news_sm')
    doc = nlp(oracion)
    palabras_clave = [token.lemma_.lower() for token in doc if token.pos_ in ['NOUN', 'ADJ'] and token.text.lower() not in STOP_WORDS]

    return palabras_clave

# Ejemplo de uso
oracion = "Yo quiero ir a la tienda a comprar queso"
palabras_clave = obtener_palabras_clave(oracion)
salida = ' '.join(palabras_clave).upper()

print(salida) """



""" import spacy

def preprocess_text(text):
    nlp = spacy.load('es_core_news_sm')

    allowed_tags = ['PRON', 'VERB', 'ADJ']

    doc = nlp(text)

    processed_text = []

    for token in doc:
        if not token.is_stop and token.pos_ in allowed_tags:
            lemma = token.lemma_
            processed_text.append(lemma)

    return processed_text

text = "Yo quiero ir a la tienda a comprar queso"
processed_text = preprocess_text(text)
print(processed_text) """


import spacy

def preprocess_text(text):
    # Aqui cargamos el modelo spañol de Spacy
    nlp = spacy.load('es_core_news_sm')

    # Se definen los STOP WORDS excluyendo los prononmbres y terminos a utilizar 
    stop_words = set(['además', 'ante', 'bajo', 'cabe', 'con', 'contra', 'cuando', 'de', 'desde', 'donde', 'durante',
                      'e', 'a', 'el', 'en', 'entre', 'hacia', 'hasta', 'la', 'las', 'lo', 'los', 'mis', 'para',
                      'por', 'qué', 'según', 'sin', 'sobre', 'tras', 'un', 'una'])

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
text = "Karlos quiere comprar un sueter"
processed_text = preprocess_text(text)
print(processed_text)
