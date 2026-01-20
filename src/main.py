from scrape import parse_url
from fastapi import FastAPI
from pydantic import BaseModel


API = FastAPI()

class FetchRequest(BaseModel):
    url : str


@API.post("/fetch_url_text")
def fetch_url_text(data: FetchRequest):
    text = parse_url(data.url)
    return {"text" : text}