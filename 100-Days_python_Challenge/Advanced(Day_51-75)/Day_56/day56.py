# Day 56: Decision Trees and Random Forests
# This script demonstrates decision trees and random forests using Scikit-learn on the Iris dataset.
# We train, evaluate, and compare the models, including feature importance visualization.

# Import necessary libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
import numpy as np

# Step 1: Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

print("Dataset: Iris")
print(f"Samples: {X.shape[0]}, Features: {X.shape[1]}, Classes: {iris.target_names}")
print()

# Step 2: Split into train/test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Train Decision Tree Classifier
dt_model = DecisionTreeClassifier(random_state=42, max_depth=3)  # Limit depth to avoid overfitting
dt_model.fit(X_train, y_train)
y_pred_dt = dt_model.predict(X_test)

print("Decision Tree Results:")
print(f"Accuracy: {accuracy_score(y_test, y_pred_dt):.2f}")
print("Classification Report:")
print(classification_report(y_test, y_pred_dt, target_names=iris.target_names))
print()

# Step 4: Train Random Forest Classifier
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)  # 100 trees in the forest
rf_model.fit(X_train, y_train)
y_pred_rf = rf_model.predict(X_test)

print("Random Forest Results:")
print(f"Accuracy: {accuracy_score(y_test, y_pred_rf):.2f}")
print("Classification Report:")
print(classification_report(y_test, y_pred_rf, target_names=iris.target_names))
print()

# Step 5: Feature Importance
# Decision Tree Feature Importance
dt_importance = dt_model.feature_importances_
print("Decision Tree Feature Importances:")
for i, imp in enumerate(dt_importance):
    print(f"{iris.feature_names[i]}: {imp:.2f}")

# Random Forest Feature Importance
rf_importance = rf_model.feature_importances_
print("\nRandom Forest Feature Importances:")
for i, imp in enumerate(rf_importance):
    print(f"{iris.feature_names[i]}: {imp:.2f}")

# Plot Feature Importances
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].barh(iris.feature_names, dt_importance, color='skyblue')
axes[0].set_title('Decision Tree Feature Importance')
axes[0].set_xlabel('Importance')

axes[1].barh(iris.feature_names, rf_importance, color='lightgreen')
axes[1].set_title('Random Forest Feature Importance')
axes[1].set_xlabel('Importance')

plt.tight_layout()
plt.show()

# Insight: Random forests often outperform single trees by reducing variance. Feature importance helps interpret models.

# Next steps: Visualize a decision tree with plot_tree, tune hyperparameters with GridSearchCV, or apply to regression.
