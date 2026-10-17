# GramPulse AI - System Architecture

## 1. Introduction

GramPulse AI is an AI-powered cash flow prediction and
financial risk alert system for rural micro-enterprises.

## 2. Main Components

### Frontend
Collects financial details and displays analysis results
through a simple web dashboard.

### Backend
Uses FastAPI to receive financial information, calculate
net cash flow, classify risk, and return recommendations.

### Machine Learning
Uses Linear Regression to demonstrate cash flow
prediction from historical sample data.

### Dataset
Contains sample monthly income, expenses, loan repayments,
and savings records.

## 3. System Workflow

Rural Entrepreneur
        |
        v
Frontend Dashboard
        |
        v
FastAPI Backend
        |
        v
Financial Data Processing
        |
        v
Cash Flow and Risk Analysis
        |
        v
Results and Recommendations

The separate ML script demonstrates historical-data
forecasting and is not currently connected to the API.

## 4. Technologies

- HTML
- CSS
- JavaScript
- Python
- FastAPI
- NumPy
- Scikit-learn

## 5. Future Enhancements

- Secure user authentication
- Database integration
- Seasonal business forecasting
- Authorized digital payment integration
- Local-language support
- Field officer dashboard

## 6. Disclaimer

This is an educational prototype using synthetic data
and simplified financial calculations. Its risk labels
and forecasts are not validated lending assessments.
