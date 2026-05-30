import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_DIR = os.path.join(BASE_DIR, "ml_models")
MODEL_PATH = os.path.join(MODEL_DIR, "student_pass_model.joblib")


def train_model():
    data = {
        "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 2, 9, 10, 3, 6, 5, 8],
        "attendance": [40, 50, 55, 60, 65, 70, 80, 90, 45, 95, 98, 58, 75, 68, 88],
        "previous_marks": [30, 35, 40, 45, 50, 55, 65, 75, 33, 85, 90, 42, 60, 52, 78],
        "assignment_score": [20, 30, 35, 40, 45, 55, 65, 80, 25, 90, 95, 38, 70, 50, 85],
        "passed": [0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
    }

    df = pd.DataFrame(data=data)

    X = df[['study_hours', 'attendance', 'previous_marks', 'assignment_score']]
    y = df['passed']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42
    )

    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ('model', LogisticRegression())
    ])

    pipeline.fit(X_train, y_train)

    predictions = pipeline.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    os.mkdir(MODEL_DIR)

    joblib.dump(pipeline, MODEL_PATH)

    print(f"Model Saved at: {MODEL_PATH}")
    print(f"Accuracy: {accuracy:2f}")


if __name__ == "__main__":
    train_model()
