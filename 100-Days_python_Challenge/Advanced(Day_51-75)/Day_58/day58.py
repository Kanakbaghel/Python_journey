# Day 58: K-Nearest Neighbors (KNN)
# This script demonstrates KNN for classification using Scikit-learn on the Iris dataset.
# We train models with different k values, evaluate, and visualize decision boundaries.

# Import necessary libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
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

# Step 3: Train and Evaluate KNN with different k values
k_values = [1, 3, 5, 7]
accuracies = []

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    accuracies.append(acc)
    
    print(f"KNN with k={k}:")
    print(f"Accuracy: {acc:.2f}")
    if k == 3:  # Detailed report for one k
        print("Classification Report:")
        print(classification_report(y_test, y_pred, target_names=iris.target_names[:2]))
    print()

# Step 4: Visualize Decision Boundaries for k=1 and k=5
def plot_decision_boundary(model, X, y, title):
    h = 0.02  # Step size in the mesh
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    
    plt.contourf(xx, yy, Z, alpha=0.8, cmap=plt.cm.coolwarm)
    plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k', cmap=plt.cm.coolwarm)
    plt.xlabel(iris.feature_names[0])
    plt.ylabel(iris.feature_names[1])
    plt.title(title)

plt.figure(figsize=(12, 5))

# For k=1
knn1 = KNeighborsClassifier(n_neighbors=1)
knn1.fit(X_train, y_train)
plt.subplot(1, 2, 1)
plot_decision_boundary(knn1, X_train, y_train, 'KNN Decision Boundary (k=1)')

# For k=5
knn5 = KNeighborsClassifier(n_neighbors=5)
knn5.fit(X_train, y_train)
plt.subplot(1, 2, 2)
plot_decision_boundary(knn5, X_train, y_train, 'KNN Decision Boundary (k=5)')

plt.tight_layout()
plt.show()

# Plot Accuracy vs k
plt.figure()
plt.plot(k_values, accuracies, marker='o')
plt.xlabel('k (Number of Neighbors)')
plt.ylabel('Accuracy')
plt.title('KNN Accuracy vs k')
plt.grid(True)
plt.show()

# Insight: Low k (e.g., 1) can overfit; higher k smooths boundaries but may underfit. KNN is lazy learning—no training phase.

# Next steps: Try different distance metrics (p=1 for Manhattan), apply KNN to regression, or handle large datasets with approximations.
