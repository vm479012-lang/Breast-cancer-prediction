
import pandas as pd
import joblib

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# Load dataset
df = pd.read_csv("data/breast_cancer.csv")

# Load model
bundle = joblib.load(
    "models/best_breast_cancer_model.joblib"
)

model = bundle["model"]
feature_names = bundle["feature_names"]

# Prepare features and actual labels
X = df[feature_names]

y_true = df["diagnosis"].map({
    "Malignant": 1,
    "Benign": 0
})

# Generate predictions
y_pred = model.predict(X)

# Calculate evaluation metrics
print("\nMODEL VALIDATION RESULTS")
print("=" * 45)

print(
    "Accuracy:",
    round(accuracy_score(y_true, y_pred) * 100, 2),
    "%"
)

print("\nClassification Report:")

print(classification_report(
    y_true,
    y_pred,
    target_names=["Benign", "Malignant"]
))

print("\nConfusion Matrix:")
print(confusion_matrix(y_true, y_pred))

print("\nValidation completed!")
