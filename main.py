import os
from datetime import datetime
from typing import List, Union

import pandas as pd
from fastapi import FastAPI, HTTPException

from classes.general.schemas import DataModelIn

app = FastAPI()


def error():
    try:
        asd = 1 / 0
        raise FileNotFoundError()

    except Exception as e:
        return e


@app.get("/items/")
async def read_item():
    try:
        re = error()
        if isinstance(re, Exception):
            raise Exception
    except Exception:
        raise HTTPException(status_code=404, detail=str(re))


@app.post("/teste")
def teste(input_data: List[DataModelIn]) -> list:
    """asdasdasd"""
    temp = []
    input_data = list(input_data)
    for entry in input_data:
        temp.append(dict(entry))
    input_data = temp.copy()
    return input_data


if __name__ == "__main__":
    os.system("uvicorn main:app --reload")
