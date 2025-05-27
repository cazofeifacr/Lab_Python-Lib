# List available Gemini models using this API key
import requests
import os

GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]
LIST_MODELS_URL = "https://generativelanguage.googleapis.com/v1beta/models"
params = {"key": GEMINI_API_KEY}

response = requests.get(LIST_MODELS_URL, params=params)
print(response.status_code)
print(response.json())
