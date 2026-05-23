from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

from pathlib import Path
import joblib
import matplotlib.pyplot as plt

PROJECT_FOLDER = Path(__file__).parent
# 1. Load the Iris dataset

iris = load_iris()

X = iris.data
y = iris.target

print("Dataset loaded successfully.")
print("Feature names:", iris.feature_names)
print("Target names:", iris.target_names)
print("Number of samples:", len(X))
print("-" * 60)


# 2. Split data into training and testing sets

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Data split completed.")
print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))
print("-" * 60)


# 3. Scale the data

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("Feature scaling completed.")
print("-" * 60)


# 4. Train the main KNN model

knn_model = KNeighborsClassifier(n_neighbors=3)

knn_model.fit(X_train_scaled, y_train)

y_pred = knn_model.predict(X_test_scaled)

accuracy = accuracy_score(y_test, y_pred)

print("Main KNN Model Evaluation")
print("Accuracy:", accuracy)
print("-" * 60)

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("-" * 60)

print("Classification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))
print("-" * 60)


# 5. Test different K values for KNN

k_values = [1, 3, 5, 7, 9]
k_accuracies = []

print("Testing Different K Values")

for k in k_values:
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train_scaled, y_train)

    predictions = model.predict(X_test_scaled)
    k_accuracy = accuracy_score(y_test, predictions)

    k_accuracies.append(k_accuracy)

    print(f"K = {k}, Accuracy = {k_accuracy}")

print("-" * 60)


# 6. Compare multiple classification algorithms

models = {
    "KNN": KNeighborsClassifier(n_neighbors=3),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Logistic Regression": LogisticRegression(max_iter=200),
    "Random Forest": RandomForestClassifier(random_state=42)
}

algorithm_results = {}

print("Comparing Multiple Classification Algorithms")

for model_name, model in models.items():
    model.fit(X_train_scaled, y_train)

    predictions = model.predict(X_test_scaled)
    model_accuracy = accuracy_score(y_test, predictions)

    algorithm_results[model_name] = model_accuracy

    print(f"{model_name}: Accuracy = {model_accuracy}")

best_algorithm = max(algorithm_results, key=algorithm_results.get)

print("Best Algorithm:", best_algorithm)
print("Best Accuracy:", algorithm_results[best_algorithm])
print("-" * 60)


# 7. Cross-validation

print("Cross-Validation Results")

for model_name, model in models.items():
    scores = cross_val_score(model, X, y, cv=5)

    print(f"{model_name}:")
    print("Scores:", scores)
    print("Average Accuracy:", scores.mean())
    print()

print("-" * 60)


# 8. Save the trained model and scaler

model_path = PROJECT_FOLDER / "knn_iris_model.pkl"
scaler_path = PROJECT_FOLDER / "scaler.pkl"

joblib.dump(knn_model, model_path)
joblib.dump(scaler, scaler_path)

print(f"Model saved as {model_path}")
print(f"Scaler saved as {scaler_path}")
print("-" * 60)


# 9. Load the saved model and scaler

loaded_model = joblib.load(model_path)
loaded_scaler = joblib.load(scaler_path)

print("Saved model and scaler loaded successfully.")
print("-" * 60)


# 10. Predict a hardcoded new flower sample

new_flower = [[5.1, 3.5, 1.4, 0.2]]

new_flower_scaled = loaded_scaler.transform(new_flower)

prediction = loaded_model.predict(new_flower_scaled)

predicted_species = iris.target_names[prediction[0]]

print("Hardcoded New Flower Prediction")
print("Input measurements:", new_flower[0])
print("Predicted species:", predicted_species)
print("-" * 60)


# 11. User input prediction

print("User Input Prediction")
print("Enter flower measurements in centimeters.")

try:
    sepal_length = float(input("Enter sepal length: "))
    sepal_width = float(input("Enter sepal width: "))
    petal_length = float(input("Enter petal length: "))
    petal_width = float(input("Enter petal width: "))

    user_flower = [[sepal_length, sepal_width, petal_length, petal_width]]

    user_flower_scaled = loaded_scaler.transform(user_flower)

    user_prediction = loaded_model.predict(user_flower_scaled)

    user_predicted_species = iris.target_names[user_prediction[0]]

    print("Your flower measurements:", user_flower[0])
    print("Predicted species:", user_predicted_species)

except ValueError:
    print("Invalid input. Please enter numeric values only.")

print("-" * 60)


# 12. Visualization: K value accuracy comparison


chart_path = PROJECT_FOLDER / "knn_k_value_accuracy.png"

plt.figure(figsize=(8, 5))
plt.plot(k_values, k_accuracies, marker="o")
plt.title("KNN Accuracy for Different K Values")
plt.xlabel("K Value")
plt.ylabel("Accuracy")
plt.grid(True)
plt.savefig(chart_path)
plt.show()

print(f"Visualization saved as {chart_path}")
