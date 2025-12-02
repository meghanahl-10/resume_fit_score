import pandas as pd

def clean_text(text):
    if pd.isna(text):
        return ""
    return text.lower().strip()

def preprocess_candidates(df):
    df["skills"] = df["skills"].apply(clean_text)
    df["education"] = df["education"].apply(clean_text)
    return df

def preprocess_jobs(df):
    df["required_skills"] = df["required_skills"].apply(clean_text)
    return df
