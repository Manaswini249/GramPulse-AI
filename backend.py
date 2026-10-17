from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="GramPulse AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)


class Finance(BaseModel):
    business_name: str
    income: float
    expenses: float
    loan: float = 0
    savings: float = 0


@app.get("/")
def home():
    return {
        "project": "GramPulse AI",
        "message": "Cash Flow Prediction API is running"
    }


@app.post("/forecast")
def forecast(data: Finance):
    net = data.income - data.expenses - data.loan

    if net < 0:
        risk = "High"
    elif data.income == 0 or net / data.income < 0.10:
        risk = "Medium"
    else:
        risk = "Low"

    recommendations = []

    if net < 0:
        recommendations.append(
            "Review business expenses and loan repayments."
        )
    else:
        recommendations.append(
            "Continue monitoring monthly cash flow."
        )

    if data.savings < data.income * 0.10:
        recommendations.append(
            "Consider building an emergency savings reserve."
        )

    return {
        "business_name": data.business_name,
        "monthly_net_cash_flow": round(net, 2),
        "three_month_projection": [
            round(net, 2),
            round(net * 2, 2),
            round(net * 3, 2)
        ],
        "risk_level": risk,
        "recommendations": recommendations
    }
