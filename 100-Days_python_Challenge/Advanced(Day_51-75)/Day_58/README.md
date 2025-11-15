# Day 58: K-Nearest Neighbors (KNN)

## Overview
Welcome to Day 58 of the 100 Days of Python Challenge for Data Science! K-Nearest Neighbors (KNN) is a simple, instance-based learning algorithm for classification and regression. It predicts by finding the 'k' closest data points (neighbors) in the feature space and voting on their labels. Today, we implement KNN classifiers using Scikit-learn on the Iris dataset, evaluate performance, and visualize decision boundaries to understand how k affects results.

## Learning Objectives
By the end of this day, you will:
- Understand KNN mechanics (distance metrics, majority voting, choosing k).
- Learn to implement KNN for classification with Scikit-learn.
- Evaluate models using accuracy and explore the impact of k on overfitting/underfitting.
- Visualize KNN decision boundaries for intuition.
- Compare KNN to distance-based models like SVM.

## Prerequisites
- Basic Python and Scikit-learn knowledge (from Days 51-57).
- Install libraries: `pip install scikit-learn matplotlib numpy`.

## Files in This Repository
- `day58_knn.py`: Python script demonstrating KNN classification and visualization.

## How to Run
1. Ensure you have Python 3.x, Scikit-learn, Matplotlib, and NumPy installed.
2. Download or clone this repository.
3. Run the script: `python day58_knn.py`.
4. Observe the output: Model training, predictions, accuracy for different k, and decision boundary plots.

## Code Explanation
The Python script (`day58_knn.py`) covers:
- Loading the Iris dataset (binary classification for simplicity).
- Splitting data and training KNN with varying k values.
- Evaluating accuracy and classification reports.
- Plotting decision boundaries to show how k influences smoothness.
- Discussing pros/cons: simplicity vs. computational cost for large datasets.

Experiment by changing k or distance metrics (e.g., Manhattan)!

## Resources
- [Scikit-learn KNN Guide](https://scikit-learn.org/stable/modules/neighbors.html)
- [KNN Explained](https://towardsdatascience.com/k-nearest-neighbors-94395f445221)
- [Decision Boundaries for KNN](https://scikit-learn.org/stable/auto_examples/neighbors/plot_classification.html)

Happy learning! If you have questions, feel free to open an issue or discuss in the challenge community.