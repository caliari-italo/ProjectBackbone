from typing import List

from fastapi import APIRouter, HTTPException

from src.general.schemas import DropList, InputData

route_one = APIRouter()


@route_one.get("/get_test/")
async def get_test(input_data: DropList):
    try:
        return input_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@route_one.post("/post_test")
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
