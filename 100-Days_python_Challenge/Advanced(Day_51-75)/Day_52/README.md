# Day 52: Data Preprocessing with Scikit-learn (Scaling, Encoding)

## Overview
Welcome to Day 52 of the 100 Days of Python Challenge for Data Science! Data preprocessing is a crucial step in machine learning pipelines, ensuring models receive clean, standardized input. Today, we focus on two key techniques using Scikit-learn: **scaling** (normalizing numerical features) and **encoding** (converting categorical features to numerical). We'll use a sample dataset to demonstrate these, preparing data for a simple classification model.

## Learning Objectives
By the end of this day, you will:
- Understand why preprocessing is essential for ML models.
- Learn to scale numerical data using StandardScaler and MinMaxScaler.
- Encode categorical data with LabelEncoder and OneHotEncoder.
- Handle basic data cleaning (e.g., missing values).
- Apply preprocessing in a pipeline and train a model on the transformed data.

## Prerequisites
- Basic Python knowledge and familiarity with Scikit-learn (from Day 51).
- Install required libraries: `pip install scikit-learn pandas numpy`.
- Knowledge of Pandas for data manipulation.

## Files in This Repository
- `day52_data_preprocessing.py`: Python script demonstrating scaling and encoding on a sample dataset.

## How to Run
1. Ensure you have Python 3.x, Scikit-learn, Pandas, and NumPy installed.
2. Download or clone this repository.
3. Run the script: `python day52_data_preprocessing.py`.
4. Observe the output: The script preprocesses data, trains a model, and evaluates it.

## Code Explanation
The Python script (`day52_data_preprocessing.py`) covers:
- Creating a sample dataset with numerical and categorical features.
- Handling missing values (imputation).
- Scaling numerical features (e.g., age, income) using StandardScaler.
- Encoding categorical features (e.g., gender, city) using OneHotEncoder.
- Training a Logistic Regression model on preprocessed data and evaluating accuracy.

Experiment by changing scalers, encoders, or adding more features!

## Resources
- [Scikit-learn Preprocessing Guide](https://scikit-learn.org/stable/modules/preprocessing.html)
- [Handling Categorical Data](https://scikit-learn.org/stable/modules/preprocessing.html#encoding-categorical-features)
- [Scaling and Normalization](https://scikit-learn.org/stable/modules/preprocessing.html#standardization-or-mean-removal-and-variance-scaling)

Happy learning! If you have questions, feel free to open an issue or discuss in the challenge community.