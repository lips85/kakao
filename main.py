import uvicorn
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class HelloResponse(BaseModel):
    version: str
    template: dict

def create_hello_response(template: dict) -> HelloResponse:
    return HelloResponse(version="2.0", template=template)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/api/sayHello")
def say_hello():
    template = {
        "outputs": [
            {
                "simpleText": {
                    "text": "AI"
                }
            }
        ]
    }
    return create_hello_response(template)


@app.post("/api/showHello")
def show_hello():
    template = {
        "outputs": [
            {
                # "simpleImage": {
                    # "imageUrl": "https://t1.daumcdn.net/friends/prod/category/M001_friends_ryan2.jpg",
                    # "altText": "hello I'm Ryan"
                "simpleText": {
                    "text": "AI"
                }
            }
        ]
    }
    return create_hello_response(template)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
