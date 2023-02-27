from flask import Flask, request, jsonify
from langdetect import *
from iso639 import languages

app = Flask(__name__)


def detect_language(text):
    """
    Detects the language of the input text and returns the language name,
    probability, reliability, and ISO 639-1 language code.

    Parameters:
    -----------
    text : str
        The input text to be analyzed for its language.

    Returns:
    --------
    Tuple[str, float, bool, str]
        A tuple containing the following elements:
        1. str: the full name of the language
        2. float: the probability that the detected language is correct, in %
        3. bool: whether the result is reliable (probability > 50%)
        4. str: the ISO 639-1 code for the detected language
    """
    result = detect_langs(text)  # Check the language(s) of the input text
    best = result[0]  # Take the best result (highest probability)
    prob = best.prob * 100  # Calculate the probability as a percentage
    short = best.lang  # Get the ISO 639-1 language code
    is_reliable = best.prob > 0.5  # Determine if the result is reliable
    long = languages.get(part1=short)  # Look up the full language name based on the ISO 639-1 code

    # Return a tuple with the language name, probability, reliability, and ISO code
    return long.name, prob, is_reliable, short


@app.route('/detect')
def detect():
    """
    Flask endpoint that detects the language of the input text.

    Parameters:
    -----------
    None

    Returns:
    --------
    Flask response object
        A response object containing the language name, probability, reliability,
        and ISO 639-1 code of the detected language, in JSON format.
    """
    text = request.args.get("text")  # Get the input text from the request arguments
    result = detect_language(text)  # Detect the language of the input text
    return jsonify(result)  # Return the result as a JSON response


if __name__ == '__main__':
    app.run(debug=False)
