# Day 55: Logistic Regression and Classification Metrics

## Overview
Welcome to Day 55 of the 100 Days of Python Challenge for Data Science! Logistic regression is a fundamental algorithm for binary classification, using the sigmoid function to predict probabilities. Today, we implement it with Scikit-learn, train on a dataset, and evaluate using key classification metrics like accuracy, precision, recall, F1-score, and ROC-AUC. We'll use the Breast Cancer dataset for a real-world example.

## Learning Objectives
By the end of this day, you will:
- Understand logistic regression's mechanics (sigmoid, log-loss).
- Train a logistic regression model using Scikit-learn.
- Interpret classification metrics and the confusion matrix.
- Plot and analyze ROC curves for threshold tuning.
- Compare metrics to assess model performance on imbalanced data.

## Prerequisites
- Basic Python and Scikit-learn knowledge (from Days 51-54).
- Install libraries: `pip install scikit-learn matplotlib numpy`.

## Files in This Repository
- `day55_logistic_regression.py`: Python script demonstrating logistic regression and evaluation metrics.

## How to Run
1. Ensure you have Python 3.x, Scikit-learn, Matplotlib, and NumPy installed.
2. Download or clone this repository.
3. Run the script: `python day55_logistic_regression.py`.
4. Observe the output: Model training, predictions, metrics, and plots.

## Code Explanation
The Python script (`day55_logistic_regression.py`) covers:
- Loading the Breast Cancer dataset (binary classification: malignant/benign tumors).
- Splitting data and training a Logistic Regression model.
- Computing predictions and evaluating with confusion matrix, accuracy, precision, recall, F1-score.
- Plotting the ROC curve and calculating AUC.
- Discussing how metrics handle class imbalance.

Experiment by changing thresholds or using multiclass datasets!

## Resources
- [Scikit-learn Logistic Regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)
- [Classification Metrics Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#classification-metrics)
- [ROC and AUC Explanation](https://developers.google.com/machine-learning/crash-course/classification/roc-and-auc)

Happy learning! If you have questions, feel free to open an issue or discuss in the challenge community.