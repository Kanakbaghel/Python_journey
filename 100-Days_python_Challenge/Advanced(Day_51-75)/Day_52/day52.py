# Day 52: Data Preprocessing with Scikit-learn (Scaling, Encoding)
# This script demonstrates data preprocessing techniques: scaling numerical features and encoding categorical ones.
# We use a sample dataset, preprocess it, and train a simple Logistic Regression model.

# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Step 1: Create a sample dataset with mixed data types
# This simulates a dataset with numerical and categorical features, including missing values.
data = {
    'age': [25, 30, np.nan, 45, 50, 35],
    'income': [50000, 60000, 70000, np.nan, 80000, 55000],
    'gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'city': ['NYC', 'LA', 'NYC', 'Chicago', 'LA', 'Chicago'],
    'target': [0, 1, 0, 1, 0, 1]  # Binary classification target
}
df = pd.DataFrame(data)
print("Original Dataset:")
print(df)
print()

# Step 2: Handle missing values
# Use SimpleImputer to fill missing numerical values with the mean.
imputer = SimpleImputer(strategy='mean')
df[['age', 'income']] = imputer.fit_transform(df[['age', 'income']])
print("After Imputation:")
print(df)
print()

# Step 3: Define features and target
X = df.drop('target', axis=1)
y = df['target']

# Step 4: Preprocessing Pipeline
# - Scale numerical features (age, income) using StandardScaler.
# - Encode categorical features (gender, city) using OneHotEncoder.
numerical_features = ['age', 'income']
categorical_features = ['gender', 'city']

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_features),
        ('cat', OneHotEncoder(), categorical_features)
    ]
)

# Step 5: Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 6: Apply preprocessing
X_train_preprocessed = preprocessor.fit_transform(X_train)
X_test_preprocessed = preprocessor.transform(X_test)

print("Preprocessed Training Data Shape:", X_train_preprocessed.shape)
print("Sample Preprocessed Features (first row):", X_train_preprocessed[0])
print()

# Step 7: Train a Logistic Regression model
model = LogisticRegression(random_state=42)
model.fit(X_train_preprocessed, y_train)

# Step 8: Make predictions and evaluate
y_pred = model.predict(X_test_preprocessed)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy on Test Set: {accuracy:.2f}")

# Optional: Show feature names after encoding
encoded_feature_names = preprocessor.named_transformers_['cat'].get_feature_names_out(categorical_features)
all_feature_names = numerical_features + list(encoded_feature_names)
print("Feature Names After Preprocessing:", all_feature_names)

# Next steps: Try MinMaxScaler instead of StandardScaler, or use LabelEncoder for ordinal categories.
