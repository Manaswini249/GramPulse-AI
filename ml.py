import numpy as np
from sklearn.linear_model import LinearRegression

# Sample historical monthly cash flow data
months = np.array([
    [1], [2], [3], [4], [5], [6]
])

cash_flow = np.array([
    3500, 4000, 3800, 5000, 5200, 6000
])

# Train the prediction model
model = LinearRegression()
model.fit(months, cash_flow)

print("GRAM PULSE AI")
print("Cash Flow Prediction")
print("--------------------")

# Predict cash flow for the next three months
for month in range(7, 10):
    prediction = model.predict([[month]])[0]

    print(
        f"Month {month}: "
        f"₹{prediction:.2f}"
    )

print("--------------------")
print("Prediction completed.")
