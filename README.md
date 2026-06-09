# DecodeLabs Tasks

This repository contains my Artificial Intelligence internship tasks completed as part of the **DecodeLabs Industrial Training Kit**.

The projects are organized into separate folders. Each folder includes the source code, documentation, and relevant generated files for a specific task.

---

## Repository Overview

This internship track focuses on building a practical foundation in Artificial Intelligence through hands-on projects.

The completed projects cover:

- Rule-based AI systems
- Python control flow and dictionary-based logic
- Supervised machine learning
- Classification models
- Feature scaling
- Model evaluation
- Cross-validation
- Model saving and loading
- Interactive user-input prediction
- Content-based recommendation systems
- TF-IDF vectorization
- Cosine similarity
- Image preprocessing
- Optical Character Recognition
- Confidence filtering
- Automated OCR configuration testing
- Data visualization
- CSV reporting
- Git and GitHub version control

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
├── project-3-ai-recommendation-system/
│   ├── recommendation_system.py
│   ├── courses.csv
│   ├── requirements.txt
│   ├── README.md
│   │
│   └── generated-output/
│       ├── recommendations.csv
│       ├── recommendation_scores.png
│       └── feedback.csv
│
├── project-4-ocr-text-recognition/
│   ├── ocr_pipeline.py
│   ├── requirements.txt
│   ├── README.md
│   │
│   ├── sample-input/
│   │   └── sample_document.png
│   │
│   └── generated-output/
│       ├── 01_original.png
│       ├── 02_grayscale.png
│       ├── 03_blurred.png
│       ├── 04_deskewed.png
│       ├── 05_otsu_threshold.png
│       ├── 06_adaptive_threshold.png
│       ├── 07_annotated_output.png
│       ├── extracted_text.txt
│       ├── validated_text.txt
│       ├── ocr_confidence_report.csv
│       ├── ocr_mode_comparison.csv
│       └── ocr_summary.txt
│
└── README.md
```

---

## Projects

## Project 1: Rule-Based AI Chatbot

### Overview

Project 1 is a simple rule-based chatbot built using Python.

The chatbot responds to predefined user inputs using dictionary-based rule matching. It does not use machine learning. Instead, it follows manually written rules to simulate a basic AI conversation.

This project represents the foundation stage of the internship because it focuses on control flow, decision-making logic, user input handling, and basic chatbot behavior.

### Project Goal

The goal is to create a chatbot that can:

- Accept user input
- Clean and process input
- Match predefined commands with responses
- Continue running in a loop
- Display a help menu
- Handle unknown commands
- Exit when the user enters an exit command

### Main Features

- Greeting responses such as `hello`, `hi`, and `hey`
- Basic AI-related answers
- Basic machine learning explanations
- Basic Python explanations
- Internship and project-related answers
- A `help` command
- Exit commands such as `exit`, `bye`, `goodbye`, and `see you`
- Input cleaning using `lower()` and `strip()`
- Dictionary-based intent matching
- Continuous conversation using a `while` loop
- Fallback responses for unknown inputs

### How It Works

```text
User Input
→ Input Cleaning
→ Exit Command Check
→ Dictionary Lookup
→ Matching Response or Fallback Response
→ Repeat Until Exit
```

### Concepts Used

- Python dictionaries
- User input using `input()`
- Output using `print()`
- String methods
- Conditional statements
- `while` loops
- `break` statements
- Intent-response matching
- Fallback handling
- Rule-based AI logic

### How to Run

From the root repository folder:

```bash
python project-1-rule-based-chatbot/chatbot.py
```

On Windows, if needed:

```bash
py project-1-rule-based-chatbot/chatbot.py
```

---

## Project 2: Data Classification Using AI

### Overview

Project 2 is a supervised machine learning classification project built using Python and scikit-learn.

The project uses the built-in Iris dataset to classify flowers into one of three species based on their measurements.

The project goes beyond a basic classification task by including:

- Feature scaling
- K-Nearest Neighbors classification
- Multiple K-value testing
- Multiple algorithm comparison
- Cross-validation
- Model saving and loading
- User-input prediction
- Data visualization

### Dataset

The Iris dataset contains **150 flower samples**.

Each sample has four input features:

- Sepal length
- Sepal width
- Petal length
- Petal width

The target output is one of three flower species:

- Setosa
- Versicolor
- Virginica

### Machine Learning Workflow

```text
Iris Dataset
→ Feature and Target Separation
→ Train-Test Split
→ Feature Scaling
→ Model Training
→ Test Predictions
→ Model Evaluation
→ Cross-Validation
→ Model Saving
→ User Input Prediction
```

### Algorithms Compared

The project compares:

- K-Nearest Neighbors
- Decision Tree
- Logistic Regression
- Random Forest

### Main Features

- Dataset loading
- Feature and target separation
- Train-test split
- Feature scaling using `StandardScaler`
- KNN classification
- Accuracy calculation
- Confusion matrix
- Classification report
- Precision, recall, and F1-score
- Multiple K-value testing
- Algorithm comparison
- 5-fold cross-validation
- Model persistence using `joblib`
- Scaler persistence using `joblib`
- Interactive user prediction
- Accuracy visualization

### Example Prediction

```text
Input:
[5.1, 3.5, 1.4, 0.2]

Output:
setosa
```

### Actual Test-Split Result

```text
Accuracy: 1.0

Confusion Matrix:
[[10  0  0]
 [ 0  9  0]
 [ 0  0 11]]
```

### Cross-Validation Result Summary

```text
KNN Average Accuracy:                 0.9667
Decision Tree Average Accuracy:       0.9533
Logistic Regression Average Accuracy: 0.9733
Random Forest Average Accuracy:       0.9667
```

Although multiple models achieved 100% accuracy on the selected test split, Logistic Regression achieved the highest average cross-validation accuracy in the tested run.

### Generated Files

```text
knn_iris_model.pkl
scaler.pkl
knn_k_value_accuracy.png
```

### How to Run

```bash
python project-2-data-classification/classification_model.py
```

On Windows, if needed:

```bash
py project-2-data-classification/classification_model.py
```

---

## Project 3: AI Recommendation Logic

### Overview

Project 3 is an advanced content-based course recommendation system built using Python and scikit-learn.

The system recommends relevant courses based on the user's interests. It loads course information from an external CSV dataset, converts text into numerical vectors using TF-IDF, calculates cosine similarity, ranks the most relevant courses, and displays the Top 5 recommendations.

### Project Goal

The goal is to create a recommendation system that can:

- Accept user interests
- Match preferences with available courses
- Rank courses by relevance
- Display the strongest recommendations
- Explain why recommendations were selected
- Save recommendation results
- Collect optional user feedback

### Recommendation Workflow

```text
User Interests
→ Input Cleaning
→ Keyword Expansion
→ TF-IDF Vectorization
→ Cosine Similarity
→ Ranked Recommendations
→ Explanations
→ CSV Output
→ Visualization
→ Optional Feedback
```

### Main Features

- External CSV course dataset
- 20 available courses
- Multiple user interests
- Input cleaning
- Keyword aliases such as `ai`, `ml`, `nlp`, `web`, and `cyber`
- TF-IDF vectorization
- Cosine similarity
- Similarity percentages
- Ranked Top-5 recommendations
- Recommendation explanations
- Multiple recommendation sessions
- Help menu
- Course-list command
- Saved recommendation CSV file
- Recommendation-score chart
- Optional feedback collection

### Supported Commands

| Command     | Description                    |
| ----------- | ------------------------------ |
| `recommend` | Start a recommendation session |
| `courses`   | Display all available courses  |
| `help`      | Display available commands     |
| `exit`      | Close the system               |
| `quit`      | Close the system               |
| `bye`       | Close the system               |

### Example Input

```text
python, ai, automation
```

### Example Output

```text
1. Machine Learning Fundamentals
   Level: Intermediate
   Similarity Score: 43.61%
   Why recommended: Recommended because it aligns with: python, artificial, intelligence

2. Automation with Python
   Level: Intermediate
   Similarity Score: 35.27%
   Why recommended: Recommended because it aligns with: python, automation
```

Similarity percentages may vary depending on the dataset and selected interests.

### Generated Files

```text
generated-output/recommendations.csv
generated-output/recommendation_scores.png
generated-output/feedback.csv
```

### How to Run

```bash
python project-3-ai-recommendation-system/recommendation_system.py
```

On Windows, if needed:

```bash
py project-3-ai-recommendation-system/recommendation_system.py
```

---

## Project 4: Advanced OCR Text Recognition Pipeline

### Overview

Project 4 is an advanced Optical Character Recognition pipeline built using Python, OpenCV, NumPy, and Tesseract OCR.

The system reads an image containing printed text, applies multiple image-preprocessing techniques, extracts machine-readable text, calculates word-level confidence scores, filters low-confidence detections, draws bounding boxes around validated words, and saves detailed output reports.

The project goes beyond a basic OCR implementation by testing multiple preprocessing strategies and Tesseract Page Segmentation Modes before automatically selecting the strongest configuration.

### Project Goal

The goal is to build a recognition pipeline that can:

- Load raw image input
- Improve the image using preprocessing
- Extract readable text
- Measure OCR confidence
- Filter low-confidence words
- Draw visual bounding boxes
- Compare multiple OCR configurations
- Select the strongest result automatically
- Save text output, CSV reports, and processed images

### OCR Workflow

```text
Input Image
→ Load Image
→ Deskew Image
→ Convert to Grayscale
→ Apply Gaussian Blur
→ Apply Thresholding
→ Test OCR Configurations
→ Compare Results
→ Select Best Configuration
→ Apply Confidence Filter
→ Draw Bounding Boxes
→ Save Reports
```

### Main Features

- Tesseract OCR integration
- OpenCV image processing
- Automatic Tesseract executable discovery
- Grayscale conversion
- Gaussian blur
- Automatic deskewing
- Otsu thresholding
- Adaptive thresholding
- Multiple preprocessing modes
- Multiple Tesseract PSM modes
- Automatic configuration comparison
- Automatic best-result selection
- Word-level confidence scores
- Minimum 80% confidence threshold
- Annotated bounding-box output
- Raw text output
- Validated text output
- OCR confidence CSV report
- OCR mode-comparison CSV report
- OCR summary report

### Preprocessing Modes

The pipeline tests:

```text
original_deskewed
grayscale
blurred
otsu_threshold
adaptive_threshold
```

### Tesseract Page Segmentation Modes

| PSM Mode | Description                  |
| -------- | ---------------------------- |
| `3`      | Automatic page segmentation  |
| `6`      | Single uniform block of text |
| `7`      | Single text line             |
| `11`     | Sparse scattered text        |

The system tests:

```text
5 preprocessing modes × 4 PSM modes = 20 OCR configurations
```

### Confidence Filtering

The project applies an 80% minimum confidence gate:

```python
MINIMUM_CONFIDENCE = 80.0
```

Words below the threshold remain visible in the confidence report but are excluded from the validated output and bounding-box visualization.

### Actual Test Result

The pipeline automatically selected:

```text
Selected preprocessing mode: original_deskewed
Selected Tesseract PSM mode: 3
Detected deskew angle: -0.63 degrees
```

Recognition performance:

```text
Total detected words: 24
Validated words with confidence >= 80%: 24
Validated ratio: 100.00%
Average detected-word confidence: 95.96%
```

Extracted text:

```text
It was the best of
times, it was the worst
of times, it was the age
of wisdom, it was the
age of foolishness...
```

### Generated Files

```text
01_original.png
02_grayscale.png
03_blurred.png
04_deskewed.png
05_otsu_threshold.png
06_adaptive_threshold.png
07_annotated_output.png
extracted_text.txt
validated_text.txt
ocr_confidence_report.csv
ocr_mode_comparison.csv
ocr_summary.txt
```

### Tesseract Installation Requirement

Install Python packages:

```bash
pip install pytesseract opencv-python numpy
```

Tesseract OCR must also be installed separately on Windows.

The default executable location is:

```text
C:\Program Files\Tesseract-OCR\tesseract.exe
```

### How to Run

```bash
python project-4-ocr-text-recognition/ocr_pipeline.py
```

On Windows, if needed:

```bash
py project-4-ocr-text-recognition/ocr_pipeline.py
```

---

## Technologies Used

- Python
- scikit-learn
- matplotlib
- joblib
- OpenCV
- NumPy
- Tesseract OCR
- pytesseract
- CSV
- pathlib
- Git
- GitHub

---

## Installation

Install the Python packages required for all projects:

```bash
pip install scikit-learn matplotlib joblib pytesseract opencv-python numpy
```

Tesseract OCR must also be installed separately to run Project 4.

---

## Project Status

| Project   | Title                                  | Status    |
| --------- | -------------------------------------- | --------- |
| Project 1 | Rule-Based AI Chatbot                  | Completed |
| Project 2 | Data Classification Using AI           | Completed |
| Project 3 | AI Recommendation Logic                | Completed |
| Project 4 | Advanced OCR Text Recognition Pipeline | Completed |

---

## Key Learning Outcomes

Through these projects, I practiced:

- Writing clean Python scripts
- Structuring repositories professionally
- Handling user input
- Building rule-based AI logic
- Understanding supervised learning
- Loading datasets
- Training classification models
- Evaluating model performance
- Comparing machine learning algorithms
- Applying cross-validation
- Saving and loading trained models
- Building content-based recommendation systems
- Applying TF-IDF vectorization
- Calculating cosine similarity
- Working with image preprocessing
- Integrating OCR libraries
- Using confidence thresholds
- Drawing bounding boxes
- Generating CSV reports
- Producing visual outputs
- Documenting projects using Markdown
- Using Git and GitHub for version control

---

## Author

**Mahmoud Yassin**

GitHub: [mahmoud-yassin10](https://github.com/mahmoud-yassin10)

Created as part of the DecodeLabs Artificial Intelligence Internship.
