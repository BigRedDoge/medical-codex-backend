import logging
from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import dependancies
import models
import schemas
from config import LOGGER_NAME

router = APIRouter(prefix='/languages', tags=['languages'])
logger = logging.getLogger(LOGGER_NAME)


@router.get("/", response_model=List[schemas.TranslationLanguagePair])
def get_languages(db: Session = Depends(dependancies.get_db)):
    return db.query(models.LanguagePairs).all()
