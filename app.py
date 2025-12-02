import streamlit as st
import pandas as pd
import docx2txt
import PyPDF2

# -------- TEXT EXTRACTION --------

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def extract_text_from_docx(file):
    return docx2txt.process(file)

def extract_text(file, file_type):
    if file_type == "pdf":
        return extract_text_from_pdf(file)
    elif file_type == "docx":
        return extract_text_from_docx(file)
    elif file_type == "txt":
        return file.read().decode("utf-8")
    return ""


# -------- SKILL MATCHING LOGIC --------

def calculate_fit_score(resume_text, job_skills):
    resume_text = resume_text.lower()

    matched_skills = []
    missing_skills = []

    for skill in job_skills:
        if skill.lower() in resume_text:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    total = len(job_skills)
    score = (len(matched_skills) / total) * 100 if total > 0 else 0
    score = min(score, 100)

    return round(score, 2), matched_skills, missing_skills


# -------- STREAMLIT UI --------

st.title("📄 Resume vs Job Description Match System")
st.write("Upload your resume and select a job role to calculate compatibility fit score.")

# Load job CSV
try:
    jobs_df = pd.read_csv("data/jobs_50.csv")
except:
    st.error("❌ jobs.csv not found! Add it inside data/jobs.csv")
    st.stop()

# Job dropdown
job_titles = jobs_df["title"].unique()
selected_job = st.selectbox("Select Job Role:", job_titles)

# Get job details
job_row = jobs_df[jobs_df["title"] == selected_job].iloc[0]
job_skills = [s.strip() for s in job_row["required_skills"].split(",")]

st.write(f"### 🛠 Required Skills for {selected_job}:")
st.write(", ".join(job_skills))

# Resume uploader
uploaded_file = st.file_uploader("📤 Upload Resume (PDF / DOCX / TXT)", type=["pdf", "docx", "txt"])

if uploaded_file:

    file_type = uploaded_file.name.split(".")[-1].lower()

    with st.spinner("Extracting resume text..."):
        resume_text = extract_text(uploaded_file, file_type)

    with st.spinner("Analyzing match..."):
        score, matched, missing = calculate_fit_score(resume_text, job_skills)

    st.success("Fit Score Generated! 🎯")

    # Results
    st.subheader(f"Fit Score: {score}%")

    st.write("### ✅ Matched Skills:")
    st.write(", ".join(matched) if matched else "No skills matched")

    st.write("### ❌ Missing Skills:")
    st.write(", ".join(missing) if missing else "No missing skills")

    st.write("### 📄 Extracted Resume Text:")
    st.text(resume_text)

else:
    st.info("Please upload your resume to continue.")
