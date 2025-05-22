from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class CalculationRequest(BaseModel):
	a: float
	b: float

@app.post("/add")
def add(req: CalculationRequest):
	return {"result": req.a + req.b}

@app.post("/subtract")
def subtract(req: CalculationRequest):
	return {"result": req.a - req.b}

@app.post("/multiply")
def multiply(req: CalculationRequest):
	return {"result": req.a * req.b}

@app.post("/divide")
def divide(req: CalculationRequest):
	if req.b == 0:
		raise HTTPException(status_code=400, detail="Division by zero is not allowed.")
	return {"result": req.a / req.b}


