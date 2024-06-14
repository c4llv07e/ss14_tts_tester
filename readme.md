# Space station 14 TTS tester

Dummy server API for testing your TTS code.

To use just put `sound.ogg` and/or `sound.wav` files near to the `./main.py`
file and launch it.

If you want to customize api token, use `TTS_API_TOKEN` env var.

Right now it is working with Corvax's, Sunrise's and Adventure Space's TTSes.

## Configure server

Add this to your server config:

```toml
[tts]
enabled = true
api_url = "http://localhost/"
api_token = "123"
```

## Installation

```shell
python3 -m pip install -r requirements.txt
```

Or install Flask with any other method prefered by you.
