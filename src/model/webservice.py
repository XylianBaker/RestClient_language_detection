from flask import Flask, request, jsonify
from langdetect import *
from iso639 import languages

app = Flask(__name__)


def detect_language(text):
    result = detect_langs(text)  # Ueberpruefung des
    best = result[0]  # bestes Ergebnis uebernehmen
    prob = best.prob * 100  # Wahrscheinlichkeit in % errechnen
    short = best.lang  # Iso639-Abkuerzung der Sprache
    is_reliable = best.prob > 0.5  # Ergebnis ist bei >50% vertrauenswuerdig
    long = languages.get(part1=short)  # Sprache auf Basis des ISo639-Codes ermitteln

    return long.name, prob, is_reliable, short


@app.route('/detect')
def detect():
    text = request.args.get("text")
    result = detect_language(text)
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=False)
