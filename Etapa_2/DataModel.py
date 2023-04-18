from pydantic import BaseModel

class DataModel(BaseModel):
    review_es: str


def columns(self):
        return ["review_es"]


