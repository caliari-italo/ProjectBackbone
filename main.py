import os
from datetime import datetime
from typing import Dict, List, Optional, Union

import pandas as pd
from fastapi import Body, FastAPI, File, UploadFile, status
from pydantic import BaseModel

app = FastAPI()


class DataModelIn(BaseModel):
    text: str = ""
    number: Union[str, int, float] = ""
    date: Union[str, datetime] = ""
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "text": "message",
                    "number": "1",
                    "date": "2023-12-31 15:00:00",
                },
            ]
        }
    }


@app.post("/teste")
def teste(input_data: List[DataModelIn]):
    lista = []
    for i in input_data:
        lista.append(dict(i))
    return pd.DataFrame(lista).astype(str).to_dict("records")


if __name__ == "__main__":
    os.system("uvicorn main:app --reload")
