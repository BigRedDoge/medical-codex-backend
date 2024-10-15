import logging

from fastapi import APIRouter, Depends
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import dependancies
import schemas
from func import translation
from config import LOGGER_NAME
import logging

router = APIRouter(prefix='/translate', tags=['levels'])
logger = logging.getLogger(LOGGER_NAME)


@router.post("/", response_model=schemas.Translation)
def get_translation(query: schemas.TranslationQuery, db: Session = Depends(dependancies.get_db)):
    result = translation.translate(query, db)
    
    # Wrap the result in a list to satisfy the expected structure of the response
    if isinstance(result, schemas.TranslationResult):
        return schemas.Translation(results=[result])
    
    return result  # In case of error, it will return the error dictionary


@router.post("/test", response_model=schemas.Translation)
def get_translation_test(query: schemas.TranslationQuery, db: Session = Depends(dependancies.get_db)):
    logging.info(query)
    logging.info(db.info)

    def result(number):
        return {
            "translated_name": f"translated_name{number}",
            "translated_source": f"translated_source{number}",
            "translated_uid": number
        }

    results = {"results": [
        result(i) for i in range(5)
    ]}
    return results
