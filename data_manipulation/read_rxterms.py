import os
import pathlib
import pandas as pd

# %% Define path to raw data
raw_terms_path = (pathlib.Path(os.getcwd()) / "raw_data" / "rxterms" / "RxTerms202304.txt")
raw_ingredients_path = (pathlib.Path(os.getcwd()) / "raw_data" / "rxterms" / "RxTermsIngredients202304.txt")

# %% Read raw data
raw_terms = pd.read_csv(raw_terms_path,
                        delimiter='|',
                        encoding="UTF-8",
                        dtype={'RXCUI': str, 'GENERIC_RXCUI': str, 'SXDG_RXCUI': str})
raw_ingredients = pd.read_csv(raw_ingredients_path,
                              delimiter='|',
                              encoding="UTF-8",
                              dtype={'RXCUI': str, 'ING_RXCUI': str})

# %% Column names to lowercase
raw_terms.columns = raw_terms.columns.str.lower()
raw_ingredients.columns = raw_ingredients.columns.str.lower()

# %% save data to csv file
raw_terms.to_csv(pathlib.Path(os.getcwd()) / "prepared_data" / "rxterms-terms.csv",
                 quoting=2,
                 index=False)
raw_ingredients.to_csv(pathlib.Path(os.getcwd()) / "prepared_data" / "rxterms-ing.csv",
                       quoting=2,
                       index=False)

# %% save data to json file
raw_terms.to_json(pathlib.Path(os.getcwd()) / "prepared_data" / "rxterms-terms.json",
                  orient='records')
raw_ingredients.to_json(pathlib.Path(os.getcwd()) / "prepared_data" / "rxterms-ing.json",
                        orient='records')
