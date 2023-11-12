import os
from datetime import datetime
from typing import List, Union

import numpy as np
import pandas as pd
from fastapi import FastAPI, HTTPException, Query

from src.exceptions.general_exceptions import GeneralException
from src.general.schemas import InputData

app = FastAPI()


@app.get("/get_test/")
async def get_test(
    input_data: str = Query(enum=["example1", "example2", "example3", "example4"])
):
    try:
        return input_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/post_test")
def post_test(input_data: List[InputData]) -> list:
    try:
        temp = []
        input_data = list(input_data)
        for entry in input_data:
            temp.append(dict(entry))
        input_data = temp.copy()
        return input_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    os.system("uvicorn main:app --reload")
