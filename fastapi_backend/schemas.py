from typing import List
from typing import Optional
from pydantic import BaseModel


class FuzzyResult(BaseModel):
    matching_name: str
    matching_source: str
    matching_uid: Optional[int] = None


class TranslationResult(BaseModel):
    translated_name: str
    translated_source: str
    translated_uid: Optional[int] = None

    class Config:
        orm_mode = True


# 3 in the diagram
class FuzzyMatching(BaseModel):
    results: List[FuzzyResult]


# 2 in the diagram
class FuzzyQuery(BaseModel):
    source_language: str
    query: str
    threshold: int = 10
    nb_max_results: int = 10


class TranslationLanguage(BaseModel):
    name: str
    code: str

    class Config:
        from_attributes = True


class TranslationLanguageResult(BaseModel):
    translations: List[TranslationLanguage]


# 6 in the diagram
class Translation(BaseModel):
    results: List[TranslationResult]


# 5 in the diagram
class TranslationQuery(BaseModel):
    translation_query: FuzzyResult
    target_language: str

class LastResort(BaseModel):
    query: str
    source_language: str
    target_language: str

class LastResortResponse(BaseModel):
    translation: str