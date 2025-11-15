# Day 57: Support Vector Machines (SVM)
# This script demonstrates SVM for classification using Scikit-learn on the Iris dataset.
# We train models with different kernels, evaluate, and visualize decision boundaries.

# Import necessary libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
import numpy as np

# Step 1: Load the Iris dataset (use first two features and two classes for 2D visualization)
iris = load_iris()
X = iris.data[:, :2]  # Only first two features (sepal length, sepal width) for plotting
y = iris.target

# For binary classification, select classes 0 and 1 (setosa and versicolor)
mask = y != 2
X = X[mask]
y = y[mask]

print("Dataset: Iris (Binary Classification)")
print(f"Samples: {X.shape[0]}, Features: {X.shape[1]}, Classes: {iris.target_names[:2]}")
print()

# Step 2: Split into train/test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Train SVM with Linear Kernel
svm_linear = SVC(kernel='linear', C=1.0, random_state=42)
svm_linear.fit(X_train, y_train)
y_pred_linear = svm_linear.predict(X_test)

print("SVM with Linear Kernel:")
print(f"Accuracy: {accuracy_score(y_test, y_pred_linear):.2f}")
print("Classification Report:")
print(classification_report(y_test, y_pred_linear, target_names=iris.target_names[:2]))
print(f"Support Vectors: {svm_linear.n_support_}")
print()

# Step 4: Train SVM with RBF Kernel
svm_rbf = SVC(kernel='rbf', C=1.0, gamma='scale', random_state=42)
svm_rbf.fit(X_train, y_train)
y_pred_rbf = svm_rbf.predict(X_test)

print("SVM with RBF Kernel:")
print(f"Accuracy: {accuracy_score(y_test, y_pred_rbf):.2f}")
print("Classification Report:")
print(classification_report(y_test, y_pred_rbf, target_names=iris.target_names[:2]))
print(f"Support Vectors: {svm_rbf.n_support_}")
print()

# Step 5: Visualize Decision Boundaries
def plot_decision_boundary(model, X, y, title):
    h = 0.02  # Step size in the mesh
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    
    plt.contourf(xx, yy, Z, alpha=0.8, cmap=plt.cm.coolwarm)
    plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k', cmap=plt.cm.coolwarm)
    plt.scatter(model.support_vectors_[:, 0], model.support_vectors_[:, 1], 
                s=100, facecolors='none', edgecolors='k', linewidths=1.5, label='Support Vectors')
    plt.xlabel(iris.feature_names[0])
    plt.ylabel(iris.feature_names[1])
    plt.title(title)
    plt.legend()

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plot_decision_boundary(svm_linear, X_train, y_train, 'SVM Linear Kernel')

plt.subplot(1, 2, 2)
plot_decision_boundary(svm_rbf, X_train, y_train, 'SVM RBF Kernel')

plt.tight_layout()
plt.show()

# Insight: Linear SVM works for linearly separable data; RBF handles non-linear. Support vectors define the margin.

# Next steps: Try polynomial kernel, tune C/gamma with GridSearchCV, or apply SVM to regression (SVR).
