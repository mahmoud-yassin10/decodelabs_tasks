# Project 2: Data Classification Using AI

## Overview

This project is a supervised machine learning classification model built using Python and scikit-learn for the **DecodeLabs Artificial Intelligence Internship**.

The model uses the built-in Iris dataset to classify flowers into one of three species based on flower measurements.

This project goes beyond the basic classification requirement by including:

- Feature scaling
- K-Nearest Neighbors classification
- Testing multiple K values
- Comparing multiple classification algorithms
- Cross-validation
- Model saving and loading
- User input prediction
- Data visualization

---

## Project Goal

The goal of this project is to build a basic classification model using a small dataset.

The project demonstrates how to:

- Load and understand a dataset
- Split data into training and testing sets
- Apply a classification algorithm
- Train a machine learning model
- Test the model on unseen data
- Evaluate model performance
- Use the model to predict new inputs

---

## Dataset

This project uses the built-in **Iris dataset** from scikit-learn.

The dataset contains **150 flower samples**.

Each sample has four input features:

- Sepal length
- Sepal width
- Petal length
- Petal width

The target output is the flower species:

- Setosa
- Versicolor
- Virginica

---

## Machine Learning Task

This is a classification problem.

The model receives flower measurements as input and predicts the flower species as output.

Example:

```text
Input:
[5.1, 3.5, 1.4, 0.2]

Output:
setosa
```

---

## Features

This project includes:

- Iris dataset loading
- Feature and target separation
- Train-test split
- Feature scaling using `StandardScaler`
- K-Nearest Neighbors classification
- Accuracy evaluation
- Confusion matrix
- Classification report
- Precision, recall, and F1-score
- Testing multiple K values
- Comparing multiple classification algorithms
- 5-fold cross-validation
- Model saving using `joblib`
- Scaler saving using `joblib`
- Model and scaler loading
- Hardcoded sample prediction
- User input prediction
- Visualization of KNN accuracy across different K values

---

## Algorithms Compared

The project compares the following classification algorithms:

- K-Nearest Neighbors
- Decision Tree
- Logistic Regression
- Random Forest

---

## Concepts Used

This project demonstrates the following machine learning and programming concepts:

- Supervised learning
- Classification
- Features and target labels
- Training data and testing data
- Feature scaling
- K-Nearest Neighbors
- Decision Trees
- Logistic Regression
- Random Forests
- Model fitting
- Prediction
- Accuracy
- Confusion matrix
- Precision
- Recall
- F1-score
- Cross-validation
- Model persistence
- Data visualization
- User input handling

---

## How the Model Works

```text
1. The Iris dataset is loaded from scikit-learn.
2. The dataset is separated into features (X) and target labels (y).
3. The data is split into training and testing sets.
4. The features are scaled using StandardScaler.
5. A KNN classifier is trained on the training data.
6. The model predicts the species of flowers in the test data.
7. The predictions are compared with the true answers.
8. The model is evaluated using accuracy, confusion matrix, and classification report.
9. Different K values are tested for the KNN model.
10. Multiple machine learning algorithms are compared.
11. Cross-validation is used for a fairer performance estimate.
12. The trained model and scaler are saved.
13. The model and scaler are loaded again.
14. The loaded model predicts a hardcoded flower sample.
15. The user can enter custom flower measurements.
16. A visualization chart is generated and saved.
```

---

## File Structure

```text
project-2-data-classification/
│
├── classification_model.py
├── README.md
├── knn_iris_model.pkl
├── scaler.pkl
└── knn_k_value_accuracy.png
```

---

## Requirements

Install the required packages before running the project:

```bash
pip install scikit-learn matplotlib
```

On Windows, if needed:

```bash
py -m pip install scikit-learn matplotlib
```

---

## How to Run

From the root repository folder, run:

```bash
python project-2-data-classification/classification_model.py
```

On Windows, if `python` does not work, run:

```bash
py project-2-data-classification/classification_model.py
```

---

## Example Output

```text
Dataset loaded successfully.
Feature names: ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
Target names: ['setosa' 'versicolor' 'virginica']
Number of samples: 150

Data split completed.
Training samples: 120
Testing samples: 30

Feature scaling completed.

Main KNN Model Evaluation
Accuracy: 1.0

Confusion Matrix:
[[10  0  0]
 [ 0  9  0]
 [ 0  0 11]]
```

---

## Classification Report Summary

In the tested run, the main KNN model achieved:

```text
Accuracy: 1.0
Precision: 1.00
Recall: 1.00
F1-score: 1.00
```

This means the model correctly classified all samples in the selected test split.

---

## KNN K-Value Testing

The project tests multiple K values for the KNN algorithm:

```text
K = 1, Accuracy = 1.0
K = 3, Accuracy = 1.0
K = 5, Accuracy = 1.0
K = 7, Accuracy = 1.0
K = 9, Accuracy = 1.0
```

This helps compare how the number of neighbors affects the model's performance.

---

## Algorithm Comparison

The project compares multiple machine learning algorithms.

In the tested run, the test-split results were:

```text
KNN: Accuracy = 1.0
Decision Tree: Accuracy = 1.0
Logistic Regression: Accuracy = 1.0
Random Forest: Accuracy = 1.0
```

Although all models achieved 100% accuracy on the selected test split, this does not mean every model is always perfect. The Iris dataset is small and clean, so high accuracy is expected.

---

## Cross-Validation Results

Cross-validation provides a fairer performance estimate by testing the models across multiple data splits.

In the tested run:

```text
KNN Average Cross-Validation Accuracy: 0.9667
Decision Tree Average Cross-Validation Accuracy: 0.9533
Logistic Regression Average Cross-Validation Accuracy: 0.9733
Random Forest Average Cross-Validation Accuracy: 0.9667
```

Based on cross-validation, **Logistic Regression** achieved the highest average accuracy in this run.

---

## User Input Prediction

The program allows the user to enter flower measurements manually.

Example:

```text
Enter sepal length: 5.1
Enter sepal width: 3.5
Enter petal length: 1.4
Enter petal width: 0.2

Your flower measurements: [5.1, 3.5, 1.4, 0.2]
Predicted species: setosa
```

---

## Generated Files

After running the program, the following files are generated:

```text
knn_iris_model.pkl
scaler.pkl
knn_k_value_accuracy.png
```

These files represent:

- `knn_iris_model.pkl` — the saved trained KNN model
- `scaler.pkl` — the saved feature scaler
- `knn_k_value_accuracy.png` — a chart comparing KNN accuracy across different K values

---

## Notes

The model achieved 100% accuracy on the selected test split. However, cross-validation is a better performance indicator because it evaluates the model across multiple splits of the dataset.

The strongest model by cross-validation in this run was Logistic Regression, with an average accuracy of approximately **97.33%**.

---

## Project Status

Completed.

---

## Author

**Mahmoud Yassin**

Created as part of the DecodeLabs Artificial Intelligence Internship.
