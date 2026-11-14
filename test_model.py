
import pandas as pd
import joblib
import os

# Load dataset
df = pd.read_csv("data/breast_cancer.csv")

# Load trained model
bundle = joblib.load(
    "models/best_breast_cancer_model.joblib"
)

model = bundle["model"]
feature_names = bundle["feature_names"]

# Select actual dataset records
X = df[feature_names]

# Predict first five records
predictions = model.predict(X.head(5))
probabilities = model.predict_proba(X.head(5))

print("MODEL TESTING RESULTS")
print("-" * 45)

for i in range(5):
    result = "Malignant" if predictions[i] == 1 else "Benign"

    print(f"\nRecord {i + 1}")
    print("Prediction:", result)
    print("Malignant probability:",
          round(probabilities[i][1] * 100, 2), "%")
    print("Benign probability:",
          round(probabilities[i][0] * 100, 2), "%")

print("\nModel testing completed successfully!")
