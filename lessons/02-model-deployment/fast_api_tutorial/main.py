from fastapi import FastAPI
from pydantic import BaseModel

# Define a data model for the request body
class Item(BaseModel):
    name: str

# Initiate the FastAPI app
app = FastAPI()

# Initiate the homepage of the API
@app.get("/")
def index():
    return {"message": "This is the homepage of the API "}

# Define a POST operation for the path "/greet"
@app.post("/greet")
def greet_user(item: Item):
    print(f"Received request: {item.name}")
    return {"message": f"Hello, {item.name}"}