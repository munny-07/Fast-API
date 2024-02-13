from pydantic import BaseModel

class titans(BaseModel):
    Pclass:int
    Sex:int
    Age:float
    SibSp:int
    Parch:int
    Fare:float
    Embarked:float