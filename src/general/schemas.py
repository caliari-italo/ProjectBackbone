from datetime import datetime
from enum import Enum
from typing import Union

from pydantic import BaseModel


class InputData(BaseModel):
    """ex schema"""

    text: Union[str, None] = None
    number: Union[int, float, None] = None
    date: Union[datetime, None] = None
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "text": "message example",
                    "number": 1,
                    "date": datetime(2023, 12, 31, 0, 0, 0),
                },
            ]
        }
    }


class DropList(str, Enum):
    exemple1 = "exemple1"
    exemple2 = "exemple2"
    exemple3 = "exemple3"
    exemple4 = "exemple4"
