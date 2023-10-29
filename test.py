import requests

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}

json_data = [
    {
        "date": "2023-12-31 15:00:00",
        "number": "1",
        "text": "message",
    },
]

response = requests.post("http://127.0.0.1:8000/teste", headers=headers, json=json_data)
