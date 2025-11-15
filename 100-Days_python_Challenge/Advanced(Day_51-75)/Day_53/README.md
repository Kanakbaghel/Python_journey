# Day 53: Train/Test Split and Cross-Validation

## Overview
Welcome to Day 53 of the 100 Days of Python Challenge for Data Science! Model evaluation is key to building reliable machine learning systems. Today, we explore **train/test splits** for basic validation and **cross-validation** for more robust assessment. We'll use Scikit-learn to demonstrate these techniques on the Iris dataset, training a classification model and evaluating its performance.

## Learning Objectives
By the end of this day, you will:
- Understand the importance of splitting data to avoid overfitting.
- Learn to perform train/test splits using `train_test_split`.
- Explore cross-validation methods like K-Fold and Stratified K-Fold.
- Compare model performance metrics (e.g., accuracy, precision) across splits.
- Apply these techniques to ensure generalizable models.

## Prerequisites
- Basic Python and Scikit-learn knowledge (from Days 51-52).
- Install required libraries: `pip install scikit-learn numpy`.

## Files in This Repository
- `day53_train_test_cv.py`: Python script demonstrating train/test splits and cross-validation.

## How to Run
1. Ensure you have Python 3.x and Scikit-learn installed.
2. Download or clone this repository.
3. Run the script: `python day53_train_test_cv.py`.
4. Observe the output: The script splits data, trains models, and evaluates using various methods.

## Code Explanation
The Python script (`day53_train_test_cv.py`) covers:
- Loading the Iris dataset.
- Performing a simple train/test split and evaluating a Logistic Regression model.
- Using K-Fold Cross-Validation to get average performance scores.
- Demonstrating Stratified K-Fold for imbalanced classes.
- Comparing results to highlight variability in single splits vs. CV.

Experiment by changing the number of folds or using different models!

## Resources
- [Scikit-learn Model Selection Guide](https://scikit-learn.org/stable/model_selection.html)
- [Cross-Validation in Scikit-learn](https://scikit-learn.org/stable/modules/cross_validation.html)
- [Train/Test Split Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html)

Happy learning! If you have questions, feel free to open an issue or discuss in the challenge community.