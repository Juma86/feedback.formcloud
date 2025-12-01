from fastapi import FastAPI
from pydantic import BaseModel
from dataclasses import dataclass
app = FastAPI()

@dataclass
class Key(BaseModel):
    key: str
    value: str

keys: list[Key] = list()

@app.get('/')
async def root() -> dict[str, str]:
    return {"message": "#DEPRECATED#"}

@app.post('/store-key')
async def post_store_key(key: Key) -> None:
    global keys
    keys.append(key)

@app.get('/retrieve-key/{keyname}')
async def get_retrieve_key(keyname: str) -> list[str]:
    return [ item.value for item in keys if item.key == keyname ]
