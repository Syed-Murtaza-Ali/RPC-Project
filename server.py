# Run with this http://127.0.0.1:8080/docs
# run both client and server terminals simultaneously
# uvicorn server:app --host 0.0.0.0 --port 8080 for server.py
# python client.py for client.py

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Model for input (x and y)
class Numbers(BaseModel):
    x: float
    y: float

# Add function
@app.post("/add")
def add(numbers: Numbers):
    result = numbers.x + numbers.y
    return {"result": result}

# Multiply function
@app.post("/multiply")
def multiply(numbers: Numbers):
    result = numbers.x * numbers.y
    return {"result": result}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="0.0.0.0", port=8080)
