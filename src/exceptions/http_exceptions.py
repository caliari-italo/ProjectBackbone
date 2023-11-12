from fastapi import HTTPException


class ErrorOne(HTTPException):
    def __init__(self):
        self.status_code = 900
        self.detail = "Error One"
