import pandas as pd

def calculate_skill_match(candidate_skills, job_skills):
    c_set = set([s.strip() for s in candidate_skills.split(",")])
    j_set = set([s.strip() for s in job_skills.split(",")])
    
    if len(j_set) == 0:
        return 0
    return len(c_set & j_set) / len(j_set)

def feature_engineering(candidates, jobs):
    rows = []

    for _, c in candidates.iterrows():
        for _, j in jobs.iterrows():

            skill_score = calculate_skill_match(c["skills"], j["required_skills"])

            exp_score = min(c["experience_years"] / j["min_experience"], 1)

            final_score = (skill_score * 0.7) + (exp_score * 0.3)

            rows.append({
                "candidate_id": c["candidate_id"],
                "job_id": j["job_id"],
                "skill_score": skill_score,
                "exp_score": exp_score,
                "fit_score": final_score
            })

    return pd.DataFrame(rows)
