# Day 51: Introduction to Scikit-learn
# This script demonstrates the basics of Scikit-learn using the Iris dataset.
# We load data, split it, train a Logistic Regression model, and evaluate accuracy.

# Import necessary libraries
from sklearn.datasets import load_iris  # For loading the Iris dataset
from sklearn.model_selection import train_test_split  # For splitting data
from sklearn.linear_model import LogisticRegression  # For the classification model
from sklearn.metrics import accuracy_score  # For evaluating model performance

# Step 1: Load the Iris dataset
# The Iris dataset is a built-in Scikit-learn dataset with 150 samples, 4 features (sepal/petal dimensions), and 3 classes (iris species).
iris = load_iris()
X = iris.data  # Features (4 columns: sepal length, sepal width, petal length, petal width)
y = iris.target  # Target labels (0: setosa, 1: versicolor, 2: virginica)

print("Dataset loaded successfully!")
print(f"Number of samples: {X.shape[0]}")
print(f"Number of features: {X.shape[1]}")
print(f"Classes: {iris.target_names}")

# Step 2: Split the data into training and testing sets
# We use 80% for training and 20% for testing. random_state ensures reproducibility.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"\nTraining set size: {X_train.shape[0]} samples")
print(f"Testing set size: {X_test.shape[0]} samples")

# Step 3: Train a Logistic Regression model
# Logistic Regression is a simple linear model for classification.
model = LogisticRegression(random_state=42, max_iter=200)  # max_iter for convergence
model.fit(X_train, y_train)  # Fit the model to the training data

print("\nModel trained successfully!")

# Step 4: Make predictions on the test set
y_pred = model.predict(X_test)

# Step 5: Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"\nModel Accuracy on Test Set: {accuracy:.2f}")

# Optional: Print some predictions for insight
print("\nSample Predictions:")
for i in range(5):
    print(f"Actual: {iris.target_names[y_test[i]]}, Predicted: {iris.target_names[y_pred[i]]}")

# Next steps: Experiment with other models like DecisionTreeClassifier or datasets like digits.
