# Day 57: Support Vector Machines (SVM)

## Overview
Welcome to Day 57 of the 100 Days of Python Challenge for Data Science! Support Vector Machines (SVM) are powerful supervised learning algorithms for classification and regression, aiming to find the optimal hyperplane that maximizes the margin between classes. Today, we explore SVM concepts like kernels (linear, RBF) and train models on the Iris dataset using Scikit-learn, evaluating performance and visualizing decision boundaries.

## Learning Objectives
By the end of this day, you will:
- Understand SVM fundamentals (support vectors, margins, kernels).
- Learn to implement SVM for classification with Scikit-learn.
- Experiment with different kernels and hyperparameters (C, gamma).
- Evaluate SVM models using accuracy and visualize results.
- Compare SVM to previous models (e.g., logistic regression, decision trees).

## Prerequisites
- Basic Python and Scikit-learn knowledge (from Days 51-56).
- Install libraries: `pip install scikit-learn matplotlib numpy`.

## Files in This Repository
- `day57_svm.py`: Python script demonstrating SVM classification and visualization.

## How to Run
1. Ensure you have Python 3.x, Scikit-learn, Matplotlib, and NumPy installed.
2. Download or clone this repository.
3. Run the script: `python day57_svm.py`.
4. Observe the output: Model training, predictions, accuracy, and decision boundary plots.

## Code Explanation
The Python script (`day57_svm.py`) covers:
- Loading the Iris dataset (focusing on binary classification for simplicity).
- Splitting data and training SVM with linear and RBF kernels.
- Evaluating models with accuracy and classification reports.
- Plotting decision boundaries to visualize hyperplanes and support vectors.
- Discussing kernel tricks for non-linear data.

Experiment by adjusting C (regularization) or gamma (for RBF)!

## Resources
- [Scikit-learn SVM Guide](https://scikit-learn.org/stable/modules/svm.html)
- [SVM Kernels Explained](https://towardsdatascience.com/svm-kernels-explained-6a6caeb72b5f)
- [Decision Boundaries Visualization](https://scikit-learn.org/stable/auto_examples/svm/plot_iris_svc.html)

Happy learning! If you have questions, feel free to open an issue or discuss in the challenge community.