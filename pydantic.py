from pydantic import BaseModel

class UserIn (BaseModel):
    username: str
    password: str

    class UserOut(BaseModel):
        username:str
        from fastapi import FastAPI, Body
        app = FastAPI()
        users = []

        @app.post("/users , response")