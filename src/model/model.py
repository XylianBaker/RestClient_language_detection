import requests


def language_detection(text: str):
    """
    Detects the language of the input text using the Flask API at http://127.0.0.1:5000/detect.

    Parameters:
    -----------
    text : str
        The input text whose language needs to be detected.

    Returns:
    --------
    str
        A formatted string containing the reliability, language, and probability of the detected language.
    """
    base_url = "http://127.0.0.1:5000/detect"  # The base URL of the Flask API
    response = requests.get(base_url, params={"text": text})  # Send a GET request to the API to detect the language
    response = response.json()  # Convert the response to JSON format
    # Format the response as a string containing the reliability, language, and probability of the detected language
    return f"reliable: <b>{response[2]}</b><br/>language: <b>{response[0]}</b><br/>probability: <b>{response[1]}%<b/>"


if __name__ == '__main__':
    text = "This is a test."
    print(language_detection(text))
