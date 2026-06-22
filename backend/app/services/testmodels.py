# test_models.py

import importlib
import os


try:
    genai = importlib.import_module("google.generativeai")
except ModuleNotFoundError as exc:
    raise ModuleNotFoundError(
        "google.generativeai package not found. Install it with pip install google-generativeai"
    ) from exc

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

for model in genai.list_models():
    print(model.name)
    print(model.supported_generation_methods)
    print("-" * 50)