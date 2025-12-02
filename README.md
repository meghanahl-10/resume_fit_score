Overview

A machine learning system that predicts how well a candidate’s resume matches a job description. It processes text, extracts skills and experience, and generates a 0–100% match score.

Features

Resume & job description preprocessing

Skill, experience, and education extraction

TF-IDF + numeric feature engineering

ML model training using scikit-learn

Match score + key factor explanation

Optional API & visualizations

#Project Structure
src/         # Preprocessing, feature engineering, training, prediction
models/      # Saved model
data/        # Sample inputs
notebooks/   # Experiments

#How to Run
pip install -r requirements.txt
python src/train.py
python src/predict.py

#Optional API
python src/api.py

#Output

Match score (0–100%)

Top matching factors
