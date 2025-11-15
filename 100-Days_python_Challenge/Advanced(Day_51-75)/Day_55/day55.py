# Day 55: Logistic Regression and Classification Metrics
# This script demonstrates logistic regression for binary classification and evaluates it using various metrics.
# We use the Breast Cancer dataset from Scikit-learn.

# Import necessary libraries
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, roc_curve, roc_auc_score, classification_report
)
import matplotlib.pyplot as plt
import numpy as np

# Step 1: Load the Breast Cancer dataset
# Binary classification: 0 = malignant, 1 = benign
data = load_breast_cancer()
X = data.data
y = data.target

print("Dataset: Breast Cancer Wisconsin")
print(f"Samples: {X.shape[0]}, Features: {X.shape[1]}, Classes: {data.target_names}")
print()

# Step 2: Split into train/test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Train Logistic Regression model
model = LogisticRegression(random_state=42, max_iter=1000)
model.fit(X_train, y_train)

print("Model trained successfully!")
print(f"Coefficients shape: {model.coef_.shape}, Intercept: {model.intercept_[0]:.2f}")
print()

# Step 4: Make predictions
y_pred = model.predict(X_test)
y_pred_proba = model.predict_proba(X_test)[:, 1]  # Probabilities for positive class

# Step 5: Evaluate with classification metrics
print("Classification Metrics:")
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
print(f"Precision: {precision_score(y_test, y_pred):.2f}")
print(f"Recall: {recall_score(y_test, y_pred):.2f}")
print(f"F1-Score: {f1_score(y_test, y_pred):.2f}")
print()

print("Confusion Matrix:")
cm = confusion_matrix(y_test, y_pred)
print(cm)
print("(TN, FP)")
print("(FN, TP)")
print()

print("Detailed Classification Report:")
print(classification_report(y_test, y_pred, target_names=data.target_names))
print()

# Step 6: ROC Curve and AUC
fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)
auc = roc_auc_score(y_test, y_pred_proba)

print(f"AUC Score: {auc:.2f}")

# Plot ROC Curve
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, label=f'Logistic Regression (AUC = {auc:.2f})')
plt.plot([0, 1], [0, 1], 'k--', label='Random Guess')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend()
plt.show()

# Insight: For imbalanced datasets, focus on precision/recall/F1 over accuracy. AUC measures overall separability.

# Next steps: Try multiclass logistic regression, add regularization (C parameter), or use other classifiers like SVM.
