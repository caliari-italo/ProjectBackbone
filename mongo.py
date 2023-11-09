import datetime
from typing import Union
from pymongo import MongoClient

host = HOST = "192.168.0.10"
port = PORT = 27017


class MongoDB:
    def set_client(self, host: str, port: int):
        self._client = MongoClient(host, port)

    def post(self, database_name: str, collection_name: str, data: Union[list, dict]):
        if isinstance(data, dict):
            data = [data]
        for entry in data:
            self._client[database_name][collection_name].insert_one(entry)

    def find(self, database_name: str, collection_name: str, search: dict):
        return [x for x in self._client[database_name][collection_name].find(search)]


mongo = MongoDB()
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

found = mongo.find("database1", "collection1", {"id": 1})
