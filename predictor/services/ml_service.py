import os
import joblib
import pandas as pd
from django.conf import settings


MODEL_PATH = os.path.join(
    settings.BASE_DIR,
    "ml_models",
    "student_pass_model.joblib"
)

_model = None


def load_model():
    global _model

    if _model is None:
        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(
                "ML model file not found. Run training/train_model.py first."
            )

        _model = joblib.load(MODEL_PATH)

    return _model


def predict_student_performance(data):
    model = load_model()

    input_df = pd.DataFrame([{
        "study_hours": data["study_hours"],
        "attendance": data["attendance"],
        "previous_marks": data["previous_marks"],
        "assignment_score": data["assignment_score"],
    }])

    prediction = model.predict(input_df)[0]

    probability = None
    if hasattr(model, "predict_proba"):
        probability = float(model.predict_proba(input_df)[0][1])

    result = "Pass" if prediction == 1 else "Fail"

    return {
        "prediction": result,
        "probability": probability,
    }
