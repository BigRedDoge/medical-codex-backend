import langchain
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
import dotenv
import json


dotenv.load_dotenv()

def last_resort(query: str, source_language: str, target_language: str, retries=0) -> dict:
    """
    This function is a last resort to find a translation for a query.
    It uses the langchain library to find a translation between two languages.
    """
    llm = ChatGoogleGenerativeAI(model="models/gemini-pro", convert_system_message_to_human=True)
    prompt = PromptTemplate.from_template("""
    Translate the following text from {source_language} to {target_language}:
    {query}.  Output the translation as a json object with the key "translation" and the value being the translated text.
    Do not add ```json``` to the beginning or end of the output.
    Do not add a period to the end of the word.
    """)
    response = llm.invoke(prompt.format(source_language=source_language, target_language=target_language, query=query))
    
    try:
        response = response.content
        res_json = json.loads(response)
        translation = res_json["translation"]
        print(translation)
    except (KeyError, AttributeError, json.JSONDecodeError):
        if retries < 5:
            return last_resort(query, source_language, target_language, retries=retries+1)
    return {"translation": translation}