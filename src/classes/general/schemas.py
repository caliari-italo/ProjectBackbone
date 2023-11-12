from datetime import datetime
from typing import Union

from pydantic import BaseModel


class DataModelIn(BaseModel):
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
