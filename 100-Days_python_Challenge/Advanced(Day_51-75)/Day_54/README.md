# Day 54: Linear Regression from Scratch and with Scikit-learn

## Overview
Welcome to Day 54 of the 100 Days of Python Challenge for Data Science! Linear regression is a foundational supervised learning algorithm for predicting continuous values. Today, we build it **from scratch** using NumPy (via gradient descent) and compare it with Scikit-learn's implementation. We'll use a simple dataset to train, predict, and evaluate the models using metrics like Mean Squared Error (MSE) and R² score.

## Learning Objectives
By the end of this day, you will:
- Understand the mathematics behind linear regression (hypothesis, cost function, gradient descent).
- Implement linear regression from scratch in Python.
- Use Scikit-learn's `LinearRegression` for efficient modeling.
- Evaluate regression models with train/test splits and performance metrics.
- Compare custom vs. library implementations for insights.

## Prerequisites
- Basic Python, NumPy, and Scikit-learn knowledge (from previous days).
- Install libraries: `pip install scikit-learn numpy matplotlib` (matplotlib for optional plotting).

## Files in This Repository
- `day54_linear_regression.py`: Python script implementing linear regression from scratch and with Scikit-learn.

## How to Run
1. Ensure you have Python 3.x, NumPy, Scikit-learn, and Matplotlib installed.
2. Download or clone this repository.
3. Run the script: `python day54_linear_regression.py`.
4. Observe the output: Model coefficients, predictions, and evaluation metrics.

## Code Explanation
The Python script (`day54_linear_regression.py`) includes:
- Generating a simple synthetic dataset (linear relationship with noise).
- Implementing linear regression from scratch using gradient descent to minimize MSE.
- Training Scikit-learn's `LinearRegression` on the same data.
- Evaluating both models on a test set with MSE and R².
- Optional plotting to visualize predictions vs. actuals.

Experiment by adjusting learning rates, epochs, or using real datasets like Boston Housing!

## Resources
- [Scikit-learn Linear Regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)
- [Gradient Descent Explanation](https://towardsdatascience.com/gradient-descent-explained-9b953fc0d2c)
- [Regression Metrics](https://scikit-learn.org/stable/modules/model_evaluation.html#regression-metrics)

Happy learning! If you have questions, feel free to open an issue or discuss in the challenge community.