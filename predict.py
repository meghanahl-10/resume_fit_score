import pickle
import pandas as pd

def predict_fit(skill_score, exp_score):

    with open("model/fit_model.pkl", "rb") as f:
        model = pickle.load(f)

    df = pd.DataFrame([{
        "skill_score": skill_score,
        "exp_score": exp_score
    }])

    prediction = model.predict(df)[0]

    explanation = {
        "skill_score_weight": skill_score,
        "experience_score_weight": exp_score
    }

    return prediction, explanation
