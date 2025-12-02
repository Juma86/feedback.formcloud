from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dataclasses import dataclass
from dotenv import dotenv_values
from httpx import get
from fastapi.responses import HTMLResponse

app = FastAPI()

environment : dict[str, str | None] = dotenv_values('api.env')

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

@app.get('/google')
async def get_google() -> HTMLResponse:
    google_url : str | None = environment.get('GOOGLE_URL')

    if google_url is None:
        raise HTTPException(status_code=500, detail='Unable to load URL of google.')

    assert google_url is not None, "No HTTPException was raised where google_url is none"

    response = get(google_url)

    if (status := response.status_code) != 200:
        raise HTTPException(status_code=502, detail='Failed to read HTML from google_url, client returned code {}'.format(status))
    
    return HTMLResponse(response.text)
