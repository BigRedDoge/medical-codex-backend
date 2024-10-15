import pandas as pd
import logging
import schemas

def translate(query: schemas.TranslationQuery, db=None):
    # Load the CSV data
    csv_file = 'fastapi_backend/database/wikidata_names.csv'
    df = pd.read_csv(csv_file)

    # Extract the necessary information from the query
    source_term = query.translation_query.matching_name  # The name to be translated
    source_language = query.translation_query.matching_source  # The source language code
    target_language = query.target_language  # The target language code

    # Mapping language codes to CSV columns
    language_map = {
        'English': 'label_en',
        'Russian': 'label_ru',
        'Ukrainian': 'label_uk',
        'French': 'label_fr'
    }

    if source_language not in language_map or target_language not in language_map:
        logging.error(f"Unsupported source or target language: {source_language}, {target_language}")
        return {"error": "Unsupported language"}, 400

    source_col = language_map[source_language]
    target_col = language_map[target_language]

    # Filter the CSV to find the source term
    try:
        result = df[df[source_col].str.lower() == source_term.lower()]

        if result.empty:
            logging.error(f"No translation found for {source_term} in {source_language}")
            return {"error": f"No translation found for {source_term}"}, 404

        # Get the translation
        translated_name = result[target_col].values[0]

        # Return the translation result as a single object
        return schemas.TranslationResult(
            translated_name=translated_name,
            translated_source=target_language,
            translated_uid=None  # Remove or set UID if needed
        )

    except Exception as e:
        logging.error(f"Error during translation: {e}")
        return {"error": "An error occurred during translation"}, 500
