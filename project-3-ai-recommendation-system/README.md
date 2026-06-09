# Project 3: AI Recommendation Logic

## Overview

This project is an advanced **content-based course recommendation system** built using Python for the **DecodeLabs Artificial Intelligence Internship**.

The system recommends relevant courses based on the user's interests. It loads course information from an external CSV dataset, converts text into numerical vectors using **TF-IDF**, measures similarity using **cosine similarity**, ranks the most relevant courses, and displays the top recommendations with similarity percentages.

The project goes beyond basic tag matching by adding:

- TF-IDF vectorization
- Cosine similarity
- Ranked Top-5 recommendations
- Keyword aliases
- Recommendation explanations
- Repeated recommendation sessions
- CSV output generation
- Visualization charts
- Optional user feedback

---

## Project Goal

The goal of this project is to create a recommendation system that can:

- Take user interests as input
- Match user preferences with available course attributes
- Rank recommendations based on similarity
- Display the most relevant items
- Explain why each recommendation was selected
- Save results for later review
- Collect optional user feedback

---

## How the Recommendation System Works

```text
1. The system loads available courses from courses.csv.
2. The user enters interests such as python, ai, or automation.
3. Keyword aliases are expanded when needed.
4. Course titles, descriptions, tags, and levels are combined into searchable text.
5. TF-IDF converts the course text and user interests into numerical vectors.
6. Cosine similarity measures how closely each course aligns with the user's interests.
7. Courses are ranked from highest to lowest similarity score.
8. The top 5 recommendations are displayed.
9. The recommendations are saved to a CSV file.
10. A visualization chart is generated.
11. The user can optionally rate the recommendations.
```

---

## Main Features

- Loads course data from an external CSV file
- Supports 20 available courses
- Accepts multiple user interests separated by commas
- Cleans user input using lowercase conversion and whitespace removal
- Supports aliases such as `ai`, `ml`, `nlp`, `web`, and `cyber`
- Uses TF-IDF vectorization
- Uses cosine similarity
- Calculates similarity percentages
- Displays ranked Top-5 recommendations
- Explains why each recommendation was selected
- Supports multiple recommendation sessions
- Includes a help menu
- Displays all available courses
- Saves recommendation results to CSV
- Generates a recommendation score chart
- Saves optional user feedback

---

## Technologies Used

- Python
- CSV
- pathlib
- scikit-learn
- matplotlib
- TF-IDF Vectorization
- Cosine Similarity
- Git
- GitHub

---

## File Structure

```text
project-3-ai-recommendation-system/
│
├── recommendation_system.py
├── courses.csv
├── requirements.txt
├── README.md
│
└── generated-output/
    ├── recommendations.csv
    ├── recommendation_scores.png
    └── feedback.csv
```

---

## Dataset

The system uses:

```text
courses.csv
```

The dataset contains 20 courses.

Each course includes:

| Column        | Description              |
| ------------- | ------------------------ |
| `course_id`   | Unique course identifier |
| `title`       | Course title             |
| `description` | Course summary           |
| `tags`        | Relevant keywords        |
| `level`       | Difficulty level         |

Example:

```csv
course_id,title,description,tags,level
1,Python for Beginners,"Learn Python syntax, variables, loops, functions, and basic programming concepts.","python programming beginner coding",Beginner
```

---

## Available Course Categories

The dataset includes courses related to:

- Python
- Artificial Intelligence
- Machine Learning
- Deep Learning
- Data Science
- Automation
- Algorithms
- Web Development
- Frontend Development
- Backend Development
- Cloud Computing
- AWS
- Cybersecurity
- Databases
- SQL
- Natural Language Processing
- Recommendation Systems
- Flutter
- Git and GitHub
- Software Engineering

---

## Recommendation Logic

### 1. User Input

The system asks the user to enter interests separated by commas.

Example:

```text
python, ai, automation
```

### 2. Keyword Expansion

The system supports aliases.

Examples:

```text
ai  → artificial intelligence
ml  → machine learning
dl  → deep learning
nlp → natural language processing
web → web development
```

### 3. TF-IDF Vectorization

TF-IDF converts text into numerical vectors.

It gives more importance to specific keywords and less importance to common words.

Example:

```text
User interests:
python artificial intelligence automation
```

The system compares these interests with each course title, description, tags, and level.

### 4. Cosine Similarity

Cosine similarity measures how closely the user's interests align with each course.

A higher score means a stronger recommendation.

Example:

```text
Machine Learning Fundamentals
Similarity Score: 47.82%
```

### 5. Ranked Recommendations

The courses are sorted from the highest similarity score to the lowest.

The system displays the Top 5 results.

---

## Supported Commands

The system supports the following commands:

| Command     | Description                        |
| ----------- | ---------------------------------- |
| `recommend` | Start a new recommendation session |
| `courses`   | Display all available courses      |
| `help`      | Display available commands         |
| `exit`      | Close the program                  |
| `quit`      | Close the program                  |
| `bye`       | Close the program                  |

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
python project-3-ai-recommendation-system/recommendation_system.py
```

On Windows, if `python` does not work, run:

```bash
py project-3-ai-recommendation-system/recommendation_system.py
```

---

## Example Usage

```text
DecodeLabs Advanced AI Course Recommendation System
======================================================================

Loaded 20 courses successfully.
Type 'help' to view the available commands.
Type 'recommend' to start.
Type 'exit' to close the program.

----------------------------------------------------------------------

Command: recommend

Enter your interests separated by commas.
Example: python, ai, automation
Aliases such as ml, ai, nlp, web, and cyber are supported.
----------------------------------------------------------------------

Your interests: python, ai, automation

Top Recommended Courses
======================================================================

1. Machine Learning Fundamentals
   Level: Intermediate
   Similarity Score: 43.61%
   Description: Understand supervised learning, classification, regression, datasets, and model evaluation using Python.
   Why recommended: Recommended because it aligns with: python, artificial, intelligence

----------------------------------------------------------------------

2. Automation with Python
   Level: Intermediate
   Similarity Score: 35.27%
   Description: Automate repetitive tasks using Python scripts, file handling, and workflow automation.
   Why recommended: Recommended because it aligns with: python, automation

----------------------------------------------------------------------

Optional Feedback
----------------------------------------------------------------------

Rate the recommendations from 1 to 5, or press Enter to skip: 5

Feedback saved successfully.

----------------------------------------------------------------------

Command: exit

Recommendation system closed. Goodbye.
```

Similarity percentages may vary depending on the dataset and user interests.

---

## Generated Files

After running the program, the system generates:

```text
generated-output/recommendations.csv
generated-output/recommendation_scores.png
generated-output/feedback.csv
```

### `recommendations.csv`

Stores the latest ranked recommendations.

Example columns:

```text
rank
user_interests
course_id
title
level
similarity_percentage
description
```

### `recommendation_scores.png`

A horizontal bar chart showing the similarity percentage of each recommended course.

### `feedback.csv`

Stores optional user feedback ratings.

Example columns:

```text
rating
top_recommendation
```

---

## Concepts Used

This project demonstrates:

- Recommendation systems
- Content-based filtering
- Pattern matching
- User preference mapping
- TF-IDF vectorization
- Cosine similarity
- Text preprocessing
- Ranking algorithms
- CSV file handling
- Input validation
- Modular Python functions
- Data visualization
- Feedback collection
- File generation
- GitHub project organization

---

## Basic Version vs Advanced Version

The initial version used simple exact tag matching:

```text
python matched → +1
automation matched → +1
```

The advanced version uses:

```text
User interests
→ keyword expansion
→ TF-IDF vectorization
→ cosine similarity
→ ranked recommendations
→ similarity percentages
```

This makes the recommendations more flexible and more relevant.

---

## Limitations

- The system recommends courses based on text similarity only.
- It does not yet learn from multiple users.
- Feedback is saved but is not yet used to update future recommendations.
- The system does not use collaborative filtering.
- The course dataset is currently limited to 20 items.

---

## Possible Future Improvements

- Use feedback ratings to improve future recommendations
- Add collaborative filtering
- Add user profiles
- Add difficulty-level filtering
- Add category filtering
- Add course duration and rating data
- Build a graphical user interface
- Convert the system into a web application
- Add database storage
- Deploy the recommendation engine online

---

## Project Status

Completed.

---

## Author

**Mahmoud Yassin**

Created as part of the DecodeLabs Artificial Intelligence Internship.
