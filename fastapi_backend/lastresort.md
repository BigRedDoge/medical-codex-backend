# Added Google Gemini for last resort route

## Setup
- Set the Gemini API key in the .env file under GOOGLE_API_KEY.

## Details
- routes/lastresort.py defines the '/lastresort' route.

- func/last_resort.py calls the Gemini API
Calls the Google Gemini API to translate a query from a source language to a target language.
It uses the langchain library to call the API.
It prompts Gemini to return the translation as a json object with the key "translation" and the value being the translated text.
It retries the translation up to 5 times if it is not a valid json or no translation is provided.

- schemas.py defines the class LastResort schema