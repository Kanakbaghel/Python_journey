# Day 54: Linear Regression from Scratch and with Scikit-learn
# This script demonstrates linear regression: implemented from scratch using gradient descent,
# and using Scikit-learn. We evaluate on a synthetic dataset.

# Import necessary libraries
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Step 1: Generate a synthetic dataset
# Simple linear relationship: y = 2*x + 3 + noise
np.random.seed(42)
X = np.random.rand(100, 1) * 10  # 100 samples, 1 feature (x values from 0 to 10)
y = 2 * X.flatten() + 3 + np.random.randn(100) * 2  # y with slope 2, intercept 3, and noise

print("Synthetic Dataset Generated:")
print(f"X shape: {X.shape}, y shape: {y.shape}")
print()

# Step 2: Split into train/test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Linear Regression from Scratch using Gradient Descent
class LinearRegressionScratch:
    def __init__(self, learning_rate=0.01, epochs=1000):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.epochs):
            y_pred = np.dot(X, self.weights) + self.bias
            dw = (1 / n_samples) * np.dot(X.T, (y_pred - y))
            db = (1 / n_samples) * np.sum(y_pred - y)

            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db

    def predict(self, X):
        return np.dot(X, self.weights) + self.bias

# Train from scratch
scratch_model = LinearRegressionScratch(learning_rate=0.01, epochs=1000)
scratch_model.fit(X_train, y_train)
y_pred_scratch = scratch_model.predict(X_test)

print("From Scratch Model:")
print(f"Weights: {scratch_model.weights}, Bias: {scratch_model.bias}")
print(f"MSE: {mean_squared_error(y_test, y_pred_scratch):.2f}, R²: {r2_score(y_test, y_pred_scratch):.2f}")
print()

# Step 4: Linear Regression with Scikit-learn
sklearn_model = LinearRegression()
sklearn_model.fit(X_train, y_train)
y_pred_sklearn = sklearn_model.predict(X_test)

print("Scikit-learn Model:")
print(f"Coefficients: {sklearn_model.coef_}, Intercept: {sklearn_model.intercept_}")
print(f"MSE: {mean_squared_error(y_test, y_pred_sklearn):.2f}, R²: {r2_score(y_test, y_pred_sklearn):.2f}")
print()

# Step 5: Optional Visualization
plt.scatter(X_test, y_test, color='blue', label='Actual')
plt.plot(X_test, y_pred_scratch, color='red', label='Scratch Prediction')
plt.plot(X_test, y_pred_sklearn, color='green', linestyle='--', label='Sklearn Prediction')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.title('Linear Regression: Actual vs Predictions')
plt.show()

# Insight: Scikit-learn uses closed-form solution (normal equation), which is faster and more accurate than gradient descent for small datasets.

# Next steps: Implement multiple linear regression, use real datasets, or add regularization (Ridge/Lasso).
