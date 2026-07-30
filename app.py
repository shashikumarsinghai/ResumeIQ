import streamlit as st
import pdfplumber
from utils.skill_extractor import extract_skills
from utils.resume_score import calculate_resume_score
from utils.job_recommender import recommend_jobs
from utils.charts import skill_chart

st.set_page_config(
    page_title="ResumeIQ-AI",
    page_icon=":robot:",
    layout="wide"
)

col1, col2 = st.columns([3, 1])

with col1:
    st.title("🤖 ResumeIQ-AI")
    st.subheader("AI-Powered Resume Analyzer")

with col2:
    st.metric("Version", "2.0")

st.write(
    """
Welcome to **ResumeIQ-AI**.

Upload your resume and let AI analyze your skills, evaluate your resume, and recommend the best career opportunities based on your profile.
"""
)

st.info("📄 Upload your resume to analyze skills, calculate ATS score, and get AI-powered job recommendations.")

st.divider()

st.header("🚀 Features")

st.markdown("""
- 📄 Upload Resume (PDF)
- 🤖  AI Resume Analysis
- 🧠 Skill Extraction
- 📊 Resume Score
- 💼 Job Recommendation
- 📈 Career Suggestions
""")

st.divider()

st.header("📂 Upload Your Resume")

uploaded_file = st.file_uploader(
    "Choose your Resume (PDF)",
    type=["pdf"]
)

if uploaded_file is not None:
    st.success("✅ Resume uploaded successfully!")
    st.write("File Name:", uploaded_file.name)

    resume_text = ""

    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                resume_text += text

    st.subheader("📄 Resume Text")

    st.text_area(
        label="Extracted Resume Text",
        value=resume_text,
        height=300
    )

    skills = extract_skills(resume_text)

    st.subheader("🧠 Extracted Skills")

    if skills:
        for skill in skills:
            st.success(skill)
    else:
        st.warning("No skills detected.")

    score, matched_skills, missing_skills = calculate_resume_score(skills)

    st.subheader("📊 Resume Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Resume Score", f"{score}/100")

    with col2:
        st.metric("Skills Found", len(skills))

    with col3:
        st.metric("Missing Skills", len(missing_skills))

    st.progress(score / 100)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("✅ Matched Skills")

        for skill in matched_skills:
            st.success(skill)

    with col2:
        st.subheader("❌ Missing Skills")

        for skill in missing_skills:
            st.error(skill)      

    st.subheader("💼 Job Recommendations")

    jobs = recommend_jobs(skills)

    for job in jobs:
        st.info(job)

    # -------Charts--------

    st.subheader("📊 Skills Analysis Chart")

    fig = skill_chart(matched_skills, missing_skills)
    
    st.pyplot(fig)

#--------Sidebar--------
st.sidebar.title("🤖 ResumeIQ-AI")

st.sidebar.markdown("---")

st.sidebar.header("📂 Resume Analyzer")

st.sidebar.info(
    """
Upload your resume and get:

✅ Skill Analysis

✅ Resume Score

✅ Job Recommendation
"""
)

st.sidebar.markdown("---")

st.sidebar.success("🚀 Phase 2 Dashboard.")

