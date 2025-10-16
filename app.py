from fastapi import FastAPI 
from pydantic import BaseModel
from joblib import load 
import numpy as np

app = FastAPI()

model = load('loan_approval_model.joblib')

class LoanRequest(BaseModel):
    income: int
    loan_amount: int
    credit_score: int

@app.post("/predict") 
def predict_loan(data: LoanRequest): 
    input_data = np.array([[data.income, data.loan_amount, data.credit_score]]) 
    prediction = model.predict(input_data)[0] 
    return {"loan_approval": "Approved" if prediction == 1 else "Rejected"}
