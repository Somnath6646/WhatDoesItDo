from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup
import openai

app = Flask(__name__)
CORS(app)

openai.api_key = ""

def get_response(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.get_text()
    truncated_text = text[0:6000]

    systemprompt = "Your Job is to tell What does this company do?"
    userprompt = truncated_text
    print(truncated_text)
    message = []
    message.append({"role": "system", "content": systemprompt})
    message.append({"role": "user", "content": userprompt})

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=message,
        temperature=0.2,
        max_tokens=4000,
        frequency_penalty=0.9
    )

    gpt_message = response.choices[0].message.content
    return gpt_message

@app.route("/get_response", methods=["POST"])
def api_description():
    data = request.get_json()
    url = data.get("url")
    print(url)
    description = get_response(url)
    return jsonify({"description": description})

if __name__ == "__main__":
    app.run()