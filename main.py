#!/usr/bin/env python3
from flask import request, Flask, abort, jsonify
import base64
import os
app = Flask(__name__)

api_token = os.environ.get("TTS_API_TOKEN", "123")

@app.route("/health", methods=["GET"])
def health():
    return "OK"

def gen_tts(text, speaker, fmt, api_key):
    if api_key != api_token:
        return "{\"error\": \"403\"}\n"
    audio_file = None
    print(api_key)
    print(text)
    print(speaker)
    print(fmt)
    if False:
        pass
    elif fmt == "ogg":
        audio_file = "./sound.ogg"
        pass
    elif fmt == "wav":
        audio_file = "./sound.wav"
        pass
    else:
        print(f"unknown format: {fmt}")
        return "{\"error\": \"501\"}\n"
    data = open(audio_file, "rb").read()
    return data

# Sunrise's API
@app.route("/", methods=["GET"], defaults={'path': ''})
@app.route("/<path:path>", methods=["GET"])
def index(path):
    req = request.args
    auth = request.headers.get("Authorization")
    if auth == None:
        print("auth fail")
        return "{\"error\": \"403\"}\n"
    api_key = auth.split()[1]
    text = req.get("text")
    speaker = req.get("speaker")
    fmt = req.get("ext")
    return gen_tts(text, speaker, fmt, api_key)

# Corvax's API
@app.route("/", methods=["POST"], defaults={'path': ''})
@app.route("/<path:path>", methods=["POST"])
def tts(path):
    req = request.json
    text = req.get("text")
    speaker = req.get("speaker")
    api_key = req.get("api_token", None)
    fmt = req.get("format")
    data = gen_tts(text, speaker, fmt, api_key)
    return jsonify({"results": [
        {"Audio": base64.b64encode(data).decode()}
    ]})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="80", debug=True)
    pass
