from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def translateToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    translatedText = machinetranslation.translator.english_to_french(textToTranslate)
    return "Translated to English: "+translatedText

@app.route("/frenchToEnglish")
def translateToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    translatedText = machinetranslation.translator.french_to_english(textToTranslate)
    return "Translated to French: "+translatedText

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
