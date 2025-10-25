# 📌 Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

# ----------------------------
# Step 1: Load California Housing dataset
# ----------------------------
housing = fetch_california_housing(as_frame=True)
df = housing.frame

print("Dataset shape:", df.shape)
print(df.head())

# Features (X) and Target (y)
X = df.drop("MedHouseVal", axis=1)  # features
y = df["MedHouseVal"]               # target (median house value in 100,000s)

# ----------------------------
# Step 2: Preprocessing
# ----------------------------
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ----------------------------
# Step 3: Train-Test Split
# ----------------------------
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# ----------------------------
# Step 4: Train Linear Regression
# ----------------------------
model = LinearRegression()
model.fit(X_train, y_train)

# ----------------------------
# Step 5: Predictions & Evaluation
# ----------------------------
y_pred = model.predict(X_test)

print("✅ Model Trained")
print("R² Score:", r2_score(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))

# ----------------------------
# Step 6: Visualization
# ----------------------------
plt.figure(figsize=(7, 5))
plt.scatter(y_test, y_pred, alpha=0.5, color="blue")
plt.xlabel("Actual Prices (100,000s USD)")
plt.ylabel("Predicted Prices (100,000s USD)")
plt.title("Actual vs Predicted House Prices")
plt.show()