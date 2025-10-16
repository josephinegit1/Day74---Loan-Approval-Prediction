import requests

url = "http://127.0.0.1:8000/predict"
data = {
    "income": 50000,
    "loan_amount": 200,
    "credit_score": 7000
}

response = requests.post(url, json=data)
print(response.json())
