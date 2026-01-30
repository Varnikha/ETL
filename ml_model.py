import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

# 1. Load the cleaned housing dataset
df = pd.read_csv("data/processed/clean_housing_data.csv")

# 2. Define target and features
target = "price"
X = df.drop(target, axis=1)
y = df[target]

# 3. Encode categorical variables
X = pd.get_dummies(X, drop_first=True)  # avoids dummy variable trap

# 4. Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 5. Train Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# 6. Make predictions
y_pred = model.predict(X_test)

# 7. Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("Model Evaluation Metrics:")
print("MAE:", mae)
print("RMSE:", rmse)
print("R² Score:", r2)

# 8. Visualize Actual vs Predicted Prices
plt.figure(figsize=(8,6))
plt.scatter(y_test, y_pred, alpha=0.7)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color="red", lw=2)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Linear Regression: Actual vs Predicted Price")
plt.show()

# 9. Insights and Limitations
print("\nInsights:")
print("- The model predicts housing prices based on numeric and categorical features.")
print("- Features like area, number of bedrooms, bathrooms, and furnishing status are influential.")
print("- Limitations: Linear Regression assumes linear relationships and may not capture complex interactions.")
print("- Future improvement: Consider scaling numeric features or trying tree-based models for better performance.")
