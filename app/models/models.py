from datetime import datetime
from typing import List
from uuid import uuid4

from pydantic import BaseModel, Field, validator


class Utils:
    def generate_id():
        return str(uuid4())

    def generate_date():
        return str(datetime.now())


class MLRequest(BaseModel):
    input_data: List[int] = Field(example=[1, 2, 3, 4])

    @validator("input_data")
    def check_len_list(cls, list_of_int):
        if not len(list_of_int) == 4:
            raise ValueError(f"{list_of_int} the number of items is not 4")
        return list_of_int


class MLResponse(BaseModel):
    id: str = Field(
        default_factory=Utils.generate_id, example="f0fabce5-17a8-4292-81b0-241bc793697c"
    )
    created_at: str = Field(
        default_factory=Utils.generate_date, example="2022-07-14 21:09:26.658815"
    )
    prediction: List[int] = Field(example=[2, 4, 6, 8])
