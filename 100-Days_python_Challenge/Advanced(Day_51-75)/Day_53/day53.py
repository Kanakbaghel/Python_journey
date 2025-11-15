# Day 53: Train/Test Split and Cross-Validation
# This script demonstrates train/test splits and cross-validation techniques using Scikit-learn.
# We use the Iris dataset and Logistic Regression to evaluate model performance.

# Import necessary libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import numpy as np

# Step 1: Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

print("Dataset loaded: Iris")
print(f"Samples: {X.shape[0]}, Features: {X.shape[1]}, Classes: {len(iris.target_names)}")
print()

# Step 2: Train/Test Split
# Split into 80% training and 20% testing. random_state for reproducibility.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Train/Test Split:")
print(f"Training samples: {X_train.shape[0]}, Testing samples: {X_test.shape[0]}")

# Train Logistic Regression on the training set
model = LogisticRegression(random_state=42, max_iter=200)
model.fit(X_train, y_train)

# Predict on test set and evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Test Accuracy: {accuracy:.2f}")
print("Classification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))
print()

# Step 3: Cross-Validation (K-Fold)
# Use 5-fold CV to get more reliable performance estimates.
cv_scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')
print("5-Fold Cross-Validation:")
print(f"CV Accuracies: {cv_scores}")
print(f"Mean CV Accuracy: {np.mean(cv_scores):.2f} ± {np.std(cv_scores):.2f}")
print()

# Step 4: Stratified K-Fold Cross-Validation
# Ensures each fold has a proportional representation of classes (useful for imbalanced data).
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
stratified_scores = cross_val_score(model, X, y, cv=skf, scoring='accuracy')
print("Stratified 5-Fold Cross-Validation:")
print(f"Stratified CV Accuracies: {stratified_scores}")
print(f"Mean Stratified CV Accuracy: {np.mean(stratified_scores):.2f} ± {np.std(stratified_scores):.2f}")
print()

# Comparison Insight
print("Insight: Single train/test split can vary due to random splits. CV provides a more stable estimate by averaging over multiple splits.")

# Next steps: Try different CV folds (e.g., 10), use other scorers like 'f1', or apply to regression models.
