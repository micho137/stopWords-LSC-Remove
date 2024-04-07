from flask import Flask, render_template, request
from script.red import preprocess_text
from script.convertToString import convertToString

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/convertText", methods=['POST'])
def convertText():
    texto = str(request.form['texto'])
    processed_text = preprocess_text(texto)
    newText = convertToString(processed_text)
    return render_template('index.html',text_converted=newText,text=texto)

if __name__ == "__main__":
    app.run(host="0.0.0.0", use_reloader=False, debug=False)