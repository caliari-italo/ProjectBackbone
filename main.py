import json
import os
from typing import Dict, List, Optional

import pandas as pd
from fastapi import Body, FastAPI, File, UploadFile, status
from pydantic import BaseModel

app = FastAPI()


class DataModelIn(BaseModel):
    message: str = None
    id: str = None
    input_data: str = None
    result: str = None
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "message": "Foo",
                    "id": "A very nice Item",
                    "input_data": "35.4",
                    "result": "3.2",
                }
            ]
        }
    }


@app.post("/teste")
def teste(input_data: List[DataModelIn]):
    lista = []
    for i in input_data:
        lista.append(dict(i))
    print(pd.DataFrame(lista).to_dict("records"))
    return pd.DataFrame(lista).to_dict("records")


if __name__ == "__main__":
    os.system("uvicorn main:app --reload")
