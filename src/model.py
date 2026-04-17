import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
df = pd.read_csv("data/bank.csv", sep=";")

# One-Hot Encoding (FIX)
df = pd.get_dummies(df, drop_first=True)

# Split features and target
X = df.drop("y_yes", axis=1)   # NOTE: target becomes y_yes
y = df["y_yes"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = DecisionTreeClassifier(
    criterion="entropy",
    max_depth=5,
    random_state=42
)

model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Save model
joblib.dump(model, "decision_tree_model.pkl")

# Save feature names
joblib.dump(X.columns.tolist(), "model_features.pkl")

print("✅ Model saved successfully!")