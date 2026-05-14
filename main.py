from fastapi import FastAPI, Header, HTTPException, Depends
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Sequential Sum API")

# Simulated secret API key (in a real app, use environment variables)
VALID_API_KEY = "super_secret_key_123"

class SumRequest(BaseModel):
    numbers: List[float]
    def length(this):
        return len(this.numbers)
    def pos(this,ind):
        return this.numbers[ind]
    def add(this):
        s=0
        for i in range(len(this.numbers)):
            s+=this.numbers[i]
        return s
def verify_api_key(x_api_key: str = Header(default=None)):
    if x_api_key != VALID_API_KEY:
        raise HTTPException(status_code=401, detail="Invalid or missing API Key")
    return x_api_key

@app.post("/sum")
def calculate_sum(payload:SumRequest, api_key: str = Depends(verify_api_key)):
    return payload.add()