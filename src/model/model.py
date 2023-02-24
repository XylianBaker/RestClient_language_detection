import requests


def language_detection(text: str):
    base_url = "http://127.0.0.1:5000/detect"
    response = requests.get(base_url, params={"text": text})
    response = response.json()
    # make the response, which looks like this: ["Somali",99.99984369234461,true,"so"]
    # into a string like this: "reliable: yes, language: Somali, probability: 99.99984369234461"
    return f"reliable: <b>{response[2]}</b><br/>language: <b>{response[0]}</b><br/>probability: <b>{response[1]}%<b/>"


if __name__ == '__main__':
    text = "This is a test."
    print(language_detection(text))
