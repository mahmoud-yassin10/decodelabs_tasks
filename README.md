# DecodeLabs Tasks

This repository contains my Artificial Intelligence internship tasks completed as part of the **DecodeLabs Industrial Training Kit**.

The tasks are organized into separate project folders. Each folder includes the source code, documentation, and generated files related to that specific task.

---

## Repository Overview

This internship track focuses on building a practical foundation in Artificial Intelligence through hands-on projects.

The completed tasks currently cover:

- Rule-based AI systems
- Python control flow and dictionary-based logic
- Supervised machine learning
- Classification models
- Model evaluation
- Cross-validation
- Model saving and loading
- User-input prediction
- Basic data visualization

---

## Repository Structure

```text
decodelabs_tasks/
│
├── project-1-rule-based-chatbot/
│   ├── chatbot.py
│   └── README.md
│
├── project-2-data-classification/
│   ├── classification_model.py
│   ├── knn_iris_model.pkl
│   ├── scaler.pkl
│   ├── knn_k_value_accuracy.png
│   └── README.md
│
└── README.md
```

---

## Projects

## Project 1: Rule-Based AI Chatbot

### Overview

Project 1 is a simple rule-based AI chatbot built using Python.

The chatbot responds to predefined user inputs using dictionary-based rule matching. It does not use machine learning yet. Instead, it follows manually written rules to simulate a basic AI conversation.

This project represents the foundation phase of the internship because it focuses on control flow, decision-making logic, input handling, and basic AI interaction.

### Project Goal

The goal of this project is to create a chatbot that can:

- Accept user input
- Understand predefined commands
- Respond with suitable answers
- Continue running in a loop
- Exit when the user enters an exit command
- Show a help menu with available commands
- Provide a fallback response for unknown inputs

### Features

- Handles greetings such as `hello`, `hi`, and `hey`
- Answers basic AI-related questions
- Answers basic Python-related questions
- Explains simple machine learning concepts
- Includes internship/project-related responses
- Supports a `help` command
- Supports exit commands such as `exit`, `bye`, `goodbye`, and `see you`
- Uses clean and organized Python code
- Uses a fallback response when the chatbot does not understand the input

### Concepts Used

- Python dictionaries
- User input with `input()`
- Output with `print()`
- String cleaning using `lower()` and `strip()`
- Conditional logic
- `while` loops
- `break` statements
- Rule-based AI logic
- Basic chatbot design

### How It Works

```text
1. The user enters a message.
2. The program cleans the input using lower() and strip().
3. The chatbot checks if the input is an exit command.
4. If not, it searches for the input inside the responses dictionary.
5. If a matching response exists, the chatbot prints it.
6. If no matching response exists, the chatbot prints a fallback message.
7. The loop continues until the user exits.
```

### How to Run Project 1

From the root repository folder:

```bash
python project-1-rule-based-chatbot/chatbot.py
```

On Windows, if `python` does not work:

```bash
py project-1-rule-based-chatbot/chatbot.py
```

### Example Commands

```text
hello
hi
what is ai
what is machine learning
what is python
what is this project about
help
exit
```

---

## Project 2: Data Classification Using AI

### Overview

Project 2 is a supervised machine learning classification project built using Python and scikit-learn.

The project uses the Iris dataset to classify flowers into one of three species based on flower measurements.

This project goes beyond the basic requirements by including:

- Feature scaling
- KNN classification
- Multiple K-value testing
- Multiple algorithm comparison
- Cross-validation
- Model saving and loading
- User input prediction
- Data visualization

### Project Goal

The goal of this project is to build a basic classification model using a small dataset.

The project demonstrates how to:

- Load and understand a dataset
- Split data into training and testing sets
- Apply a classification algorithm
- Train a machine learning model
- Test the model on unseen data
- Evaluate model performance
- Use the model to predict new inputs

### Dataset

This project uses the built-in **Iris dataset** from scikit-learn.

The dataset contains **150 flower samples**.

Each sample includes four input features:

- Sepal length
- Sepal width
- Petal length
- Petal width

The target output is the flower species:

- Setosa
- Versicolor
- Virginica

### Machine Learning Task

This is a classification problem.

The model receives flower measurements as input and predicts the flower species as output.

Example:

```text
Input:
[5.1, 3.5, 1.4, 0.2]

Output:
setosa
```

### Features

- Loads the Iris dataset
- Separates features and target labels
- Splits the data into training and testing sets
- Scales features using `StandardScaler`
- Trains a K-Nearest Neighbors model
- Evaluates the model using accuracy
- Displays a confusion matrix
- Displays a classification report
- Shows precision, recall, and F1-score
- Tests different K values for KNN
- Compares multiple classification algorithms
- Uses 5-fold cross-validation
- Saves the trained model using `joblib`
- Saves the scaler using `joblib`
- Loads the saved model again for prediction
- Allows the user to enter custom flower measurements
- Generates a visualization chart for KNN accuracy by K value

### Algorithms Compared

The project compares the following classification algorithms:

- K-Nearest Neighbors
- Decision Tree
- Logistic Regression
- Random Forest

### Concepts Used

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

### How It Works

```text
1. The Iris dataset is loaded from scikit-learn.
2. The dataset is separated into features (X) and target labels (y).
3. The data is split into training and testing sets.
4. The features are scaled using StandardScaler.
5. A KNN classifier is trained on the training data.
6. The model predicts the species of flowers in the test data.
7. The predictions are compared with the true answers.
8. The model is evaluated using accuracy, confusion matrix, and classification report.
9. Different K values are tested.
10. Multiple machine learning algorithms are compared.
11. Cross-validation is used for a fairer performance estimate.
12. The trained model and scaler are saved.
13. The model and scaler are loaded again.
14. The user can enter custom flower measurements.
15. A visualization chart is generated and saved.
```

### How to Run Project 2

From the root repository folder:

```bash
python project-2-data-classification/classification_model.py
```

On Windows, if `python` does not work:

```bash
py project-2-data-classification/classification_model.py
```

### Example Output

```text
Dataset loaded successfully.
Feature names: ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
Target names: ['setosa' 'versicolor' 'virginica']
Number of samples: 150

Main KNN Model Evaluation
Accuracy: 1.0

Confusion Matrix:
[[10  0  0]
 [ 0  9  0]
 [ 0  0 11]]
```

### Cross-Validation Result Summary

The model comparison showed strong performance across all algorithms.

In the tested run:

```text
KNN Average Cross-Validation Accuracy: 0.9667
Decision Tree Average Cross-Validation Accuracy: 0.9533
Logistic Regression Average Cross-Validation Accuracy: 0.9733
Random Forest Average Cross-Validation Accuracy: 0.9667
```

Although multiple algorithms achieved 100% accuracy on the selected test split, cross-validation provided a fairer comparison. Logistic Regression achieved the highest average cross-validation accuracy in this run.

### User Input Example

The program allows the user to enter custom flower measurements.

Example:

```text
Enter sepal length: 5.1
Enter sepal width: 3.5
Enter petal length: 1.4
Enter petal width: 0.2

Predicted species: setosa
```

### Generated Files

After running Project 2, the following files are generated:

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

## Technologies Used

- Python
- scikit-learn
- matplotlib
- joblib
- Git
- GitHub

---

## Installation

Before running the machine learning project, install the required packages:

```bash
pip install scikit-learn matplotlib
```

On Windows, if needed:

```bash
py -m pip install scikit-learn matplotlib
```

---

## Project Status

| Project | Title | Status |
|---|---|---|
| Project 1 | Rule-Based AI Chatbot | Completed |
| Project 2 | Data Classification Using AI | Completed |
| Project 3 | Coming Soon | Pending |
| Project 4 | Coming Soon | Pending |

---

## Key Learning Outcomes

Through these tasks, I practiced:

- Writing clean Python scripts
- Structuring projects professionally
- Creating rule-based AI logic
- Handling user input
- Building a basic chatbot
- Understanding supervised learning
- Loading datasets from scikit-learn
- Training classification models
- Evaluating machine learning performance
- Comparing algorithms
- Saving and reusing trained models
- Documenting projects clearly using Markdown
- Using Git and GitHub for version control and submission

---

## Author

**Mahmoud Yassin**

GitHub: [mahmoud-yassin10](https://github.com/mahmoud-yassin10)

Created as part of the DecodeLabs Artificial Intelligence Internship.