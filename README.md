# stopWords LSC Remove by Michaen Rangel
En este proyecto se usó:
* [spaCy](https://spacy.io/)(Es una librería de software para procesamiento de lenguaje natural programado en Python)
* [Flask](https://flask.palletsprojects.com/en/3.0.x/)(Framework minimalista de Python)
* [DaisyUI](https://daisyui.com/)(Libreria de componentes hechos con TailwindCSS) 
---
El objetivo de este proyecto es poder procesar y transformar oraciones del idioma español a la raiz de esta misma pero enfocada a la [lengua de señas colombiana](https://es.wikipedia.org/wiki/Lengua_de_se%C3%B1as_colombiana)
* La lengua de señas también sigue un orden de jerarquía desde lo localizado a lo localizable. Obsérvese por ejemplo la siguiente glosa: `ABUELO SOPA PASTA ALMUERZO COCINAR`. La traducción de la glosa anterior a la lengua española escrita podría ser la siguiente: `La abuela preparó sopa de pasta para el almuerzo`. ([DICCIONARIO BÁSICO DE LA LENGUA DE SEÑAS COLOMBIANA, 2011, p. 77](https://lenguasdecolombia.caroycuervo.gov.co/ICCadmin/ICC/documentos/Diccionario_lenguaje_de_se%C3%B1as_PT1.pdf))
* Para acercarnos a este objetivo tenemos que comprender varios puntos:
  1. Todos los verbos se encuentran `lematizados (la lematización es el proceso de reducir las palabras a su forma basica o forma de diccionario, conocida como el lema)` o en `infinitivo (forma no personal del verbo, cuya terminación en español es -ar, -er o -ir).`
  2. No existen conectores o por lo menos gran parte de ellos, en este caso nos referimos a ellos como [stop words](https://roincrease.net/roiwiki/stop-words/) o palabras de parada, tales como: `a, la, los, las, de, le, en, es`, entre otros más.
  3. Los nombres propios para las personas deben ser deletreados.
  4. A diferencia del idioma español, las oraciones usadas por las personas sordas en Colombia se encuentran en orden contrario, por ejemplo:
     
| Español  | Lengua de señas colombiana (LSC) |
| :-------------: | :-------------: |
| El día lunes 28 de septiembre comeré en familia | FAMILIA COMER SEPTIEMBRE 28 LUNES DIA |
| Los dias sabado y domingo salgo a bailar  | BAILAR SALIR YO DOMINGO SABADO  |
---
## Creacion del script
Para poder trabajar de manera comoda y eficiente usaremos los [entornos virtuales de Python](https://docs.python.org/es/3/library/venv.html)
```python
python -m venv venv
```
Dependiendo la terminal que estemos usando habrán maneras para activar este entorno virtual, de las siguientes maneras:

| Shell | Comando |
|---|---|
| cmd | \venv\Scripts\activate.bat |
| PowerShell | \venv\Scripts\Activate.ps1 |
| bash/zsh | source /venv/bin/acivate |

Ahora instalamos spaCy junto a sus dependencias para poder empezar a trabajar con el:
```python
pip install -U pip setuptools wheel
pip install -U spacy
python -m spacy download es_core_news_sm
```
El parametro `es_core_news_sm` nos descarga el modelo entrenado `español (es)` ligero, esto es determinado por las siglas `sm`, cabe realtar que spaCy nos permite entrenar nuestros propios modelos, pero para efectos de este proyecto usaremos dos variantes de los modelos entrenados en español.

Ahora creamos un archivo py donde vamos a importar spaCy e inicializaremos el modelo descargado, de la siguiente manera:
```python
import spacy
nlp = spacy.load("es_core_news_sm")
doc = nlp("Quiero comprar un helado para ti.")
print([(token.text, token.pos_) for token in doc])
```
y la salida obtenida es la siguiente:
```python
[('Quiero', 'VERB'), ('comprar', 'VERB'), ('un', 'DET'), ('helado', 'NOUN'), ('para', 'ADP'), ('ti', 'PRON'), ('.', 'PUNCT')]
```
De la salida podemos resaltar dos caracteristicas:
* token.text - corresponde a los elementos tokenizados e identificados dentro de la oración
* token.pos_ - corresponde al identificador gramatical para cada palabra
  * VERB = Verbo
  * DET = Determinante
  * NOUN = Sustantivo
  * PRON = Pronombre
  * ADP = Preposiciones y posposiciones
  * PUNCT = Signos de puntuación
* Aqui una tabla donde podemos encontrar todos los identificadores
  
| Type | Description |
|:---:|:---:|
| ADJ | Adjectivo |
| ADP | Preposicion y posposicion |
| ADV | Adverbio |
| AUX | Auxiliar |
| CCONJ | Conjunción coordinada |
| DET | Determinante |
| INTJ | Interjección |
| NOUN | Sustantivo |
| NUM | Número |
| PART | Particula gramatical |
| PRON | Pronombre |
| PROPN | Nombre propio |
| PUNCT | Signo de puntuación |
| SCONJ | Conjunción subordinada |
| SYM | Simbolos |
| VERB | Verbos |
| X | Otros |

Debemos ahora priorizar la convercion de las palabras, primero debemos lematizar las palabras, para ello nos apoyaremos en el identificador gramatical `VERB` y la propiedad `token.lemma_`:
```python
processed_text = []
for token in doc:
  if token.pos_ == "VERB"
      lemma = token.lemma_
      processed_text.append(lemma)
print(processed_text)
```
Nos apoyamos con un arreglo para almacenar las salidas correspondientes y observamos la salida:
```python
['querer', 'comprar']
```
A partir de ahora nos queda clasificar los nombres y tener en cuenta que no todos los stop words se excluyen dentro de la LSC
```python
if token.pos == "PROPN":
    spell = list(token.text)
    processed_text.extend(spell)
```
Si dentro del texto se encuentra un token con identificador `PROPN` entonces procedemos a crear una lista de unicaracteres, es decir, obtenemos una lista de caracteres que anexaremos al arreglo final, por ejemplo:
```python
doc = nlp("Carlos quiere comprar un helado")
processed_text = []
for token in doc:
    if token.pos_ == 'PROPN':
        spell = list(token.text)
        processed_text.extend(spell)
    else:
        if token.pos_ == 'VERB':
            lemma = token.lemma_
            processed_text.append(lemma)
print(processed_text)
```
La salida correspondiente:
```python
['C', 'a', 'r', 'l', 'o', 's', 'querer', 'comprar']
```
