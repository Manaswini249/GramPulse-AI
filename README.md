# GramPulse AI

AI-powered cash flow prediction and risk alert system
for rural micro-enterprises.

## About the Project

GramPulse AI helps rural entrepreneurs, Self-Help Groups
(SHGs), and Farmer Producer Organizations understand their
cash flow, monitor financial risks, and plan their finances.

## Key Features

- Cash flow forecasting
- Business health score
- Financial risk classification
- Loan readiness assessment
- Personalized financial recommendations
- Simple web dashboard

## Technology Stack

- Frontend: HTML, CSS, JavaScript
- Backend: Python, FastAPI
- Data Processing: Pandas
- Machine Learning: Scikit-learn
- API: REST API

## Project Structure

- backend/ - API and forecasting logic
- frontend/ - User dashboard
- ml/ - Model training script
- data/ - Sample financial records
- docs/ - Project documentation

## How to Run

1. Install Python 3.10 or newer.
2. Install backend dependencies:

   pip install -r backend/requirements.txt

3. Start the backend:

   uvicorn app.main:app --reload --app-dir backend

4. Open frontend/index.html in your browser.

Backend API documentation:
http://127.0.0.1:8000/docs

## Disclaimer

This project is a prototype for educational purposes.
Predictions use simplified sample-data assumptions and
must not be used as the sole basis for lending decisions.
