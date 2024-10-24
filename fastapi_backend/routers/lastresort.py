from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from func import last_resort
import dependancies
import models
import schemas
from config import LOGGER_NAME
import logging


router = APIRouter(prefix='/lastresort', tags=['lastresort'])
logger = logging.getLogger(LOGGER_NAME)


@router.post("/", response_model=schemas.LastResortResponse)
def get_lastresort(query: schemas.LastResort):
    print(query)
    results = last_resort.last_resort(query.query, query.source_language, query.target_language)
    print(results)
    logging.info(results)
    return results