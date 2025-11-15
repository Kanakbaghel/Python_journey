# Day 56: Decision Trees and Random Forests

## Overview
Welcome to Day 56 of the 100 Days of Python Challenge for Data Science! Decision trees are intuitive, interpretable models that split data based on features to make predictions. Random forests improve upon this by ensemble learning—combining multiple trees to reduce overfitting and boost accuracy. Today, we train both on the Iris dataset, evaluate performance, and explore feature importance.

## Learning Objectives
By the end of this day, you will:
- Understand decision tree mechanics (splitting, Gini impurity, pruning).
- Learn how random forests aggregate trees for better generalization.
- Train and compare DecisionTreeClassifier and RandomForestClassifier using Scikit-learn.
- Evaluate models with accuracy and visualize feature importance.
- Gain insights into overfitting and ensemble benefits.

## Prerequisites
- Basic Python and Scikit-learn knowledge (from Days 51-55).
- Install libraries: `pip install scikit-learn matplotlib`.

## Files in This Repository
- `day56_decision_trees_rf.py`: Python script demonstrating decision trees and random forests.

## How to Run
1. Ensure you have Python 3.x, Scikit-learn, and Matplotlib installed.
2. Download or clone this repository.
3. Run the script: `python day56_decision_trees_rf.py`.
4. Observe the output: Model training, predictions, accuracy, and feature importance plots.

## Code Explanation
The Python script (`day56_decision_trees_rf.py`) covers:
- Loading the Iris dataset (multiclass classification).
- Splitting data and training a Decision Tree model.
- Training a Random Forest ensemble.
- Evaluating both with accuracy and classification reports.
- Plotting feature importance to understand model decisions.
- Comparing results to show ensemble advantages.

Experiment by tuning hyperparameters like max_depth or n_estimators!

## Resources
- [Scikit-learn Decision Trees](https://scikit-learn.org/stable/modules/tree.html)
- [Random Forests Guide](https://scikit-learn.org/stable/modules/ensemble.html#random-forests)
- [Feature Importance](https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_importances.html)

Happy learning! If you have questions, feel free to open an issue or discuss in the challenge community.