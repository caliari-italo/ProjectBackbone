import datetime
from typing import Union
from pymongo import MongoClient
from classes.mongo_db.mongo_db_info import mongo_db_info


class MongoDB:
    def __init__(self):
        self._host = mongo_db_info["HOST"]
        self._port = mongo_db_info["PORT"]

    def connect_to_db(self):
        self._client = MongoClient(self._host, self._port)

    def post(self, database_name: str, collection_name: str, data: Union[list, dict]):
        if isinstance(data, dict):
            data = [data]
        for entry in data:
            self._client[database_name][collection_name].insert_one(entry)

    def find(self, database_name: str, collection_name: str, search: dict):
        return [x for x in self._client[database_name][collection_name].find(search)]


mongo = MongoDB()
mongo.connect_to_db()
mongo.set_client(HOST, PORT)


for i in range(10000):
    mongo.post(
        "database1",
        "collection1",
        {
            "id": i,
            "date": datetime.datetime.now(),
        },
    )

found = mongo.find("database1", "collection1", {})

found = mongo.find(
    "database1",
    "collection1",
    {
        "date": {
            "$gte": datetime.datetime(2023, 11, 9, 23, 22),
            "$lt": datetime.datetime(2023, 11, 9, 23, 25),
        },
    },
)
