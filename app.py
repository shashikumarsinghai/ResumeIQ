import streamlit as st
import pdfplumber
from utils.skill_extractor import extract_skills
from utils.resume_score import calculate_resume_score
from utils.job_recommender import recommend_jobs
from utils.charts import skill_chart
from utils.resume_feedback import generate_feedback
from utils.course_recommender import recommend_courses
from utils.pdf_report import create_pdf

st.set_page_config(
    page_title="ResumeIQ",
    page_icon="📄",
    layout="wide"
)

col1, col2 = st.columns([3, 1])

with col1:
    st.title("📄 ResumeIQ")
    st.caption("Smart Resume Analyzer • ATS Score • Career Guidance")

with col2:
    st.metric("Version", "2.0")

st.write(
"""
Upload your resume to receive an ATS score, technical skill analysis, personalized job recommendations, course suggestions, and a downloadable professional PDF report.
"""
)

st.info("📄 Upload your resume below to get started!")

st.divider()

#------- Features --------

st.header("🚀 Features")

st.markdown("""
- 📄 Upload Resume (PDF)
- 🧠 Skill Extraction
- 📊 Resume Score
- 💼 Job Recommendation
- 📈 Career Suggestions
- 📋 Resume Feedback
- 📊 Skills Visualization
""")

st.divider()

#------- Resume Upload --------

st.markdown("---")
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

#-------Resume Text Display--------

    st.subheader("📄 Extracted Resume Text")

    st.text_area(
        label="Extracted Resume Text",
        value=resume_text,
        height=300
    )

    skills = extract_skills(resume_text)

#-------Skills Extraction--------

    st.subheader("🧠 Skills Analysis")

    if skills:
        for skill in skills:
            st.success(skill)
    else:
        st.warning("No skills detected.")

    score, matched_skills, missing_skills = calculate_resume_score(skills)

#-------Resume Dashboard--------

    st.subheader("📊 Resume Analysis Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Resume Score", f"{score}/100")

    with col2:
        st.metric("Skills Found", len(skills))

    with col3:
        st.metric("Missing Skills", len(missing_skills))

    st.write(f"### Overall ATS Score : {score}/100")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("✅ Detected Skills")

        for skill in matched_skills:
            st.success(skill)

    with col2:
        st.subheader("📌 Recommended Skills")

        for skill in missing_skills:
            st.error(skill)      

#-------Job Recommendations--------
    st.subheader("💼 Recommendations for Job Roles")

    jobs = recommend_jobs(skills)

    for job in jobs:
        st.info(job)

# -------Course Recommendations--------

    st.subheader("📚 Learning Resources")

    courses = recommend_courses(missing_skills)

    if courses:
        for course in courses:
            st.info(course)

    else:
        st.success("🎉 No course recommendations. Your resume already covers all required skills!")

#-------Career Tips--------

    st.header("🎯 Career Guidance")

    if score >= 80:
        st.success("Excellent Resume! Keep updating your projects and certifications.")

    elif score >= 60:
        st.warning("Good Resume! Improve missing skills to increase your ATS score.")

    else:
        st.error("Your resume needs improvement. Learn the recommended Courses and add more projects.")          

# -------Charts--------

    st.subheader("📊 Skills Distribution")

    fig = skill_chart(matched_skills, missing_skills)
    
    st.pyplot(fig)

# -------Resume Feedback--------

    st.subheader("📋 Resume Feedback")

    feedback = generate_feedback(score, missing_skills)

    for item in feedback:
        st.write(item)

# -------Download PDF Report--------

    st.subheader("📄 Download Professional Resume Report")

    pdf_file = create_pdf(score, matched_skills, missing_skills, jobs)

    with open(pdf_file, "rb") as file:
        st.download_button(
            label="Download Professional Resume Report",
            data=file,
            file_name="Professional_Resume_Report.pdf",
            mime="application/pdf"
        )        

#--------Sidebar--------
st.sidebar.title("📋 ResumeIQ")

st.sidebar.markdown("---")

st.sidebar.header("DASHBOARD")

st.sidebar.info(
    """
Upload your resume and get:

✅ Skill Analysis

✅ Resume Score

✅ Job Recommendation
"""
)

st.sidebar.markdown("---")

st.sidebar.success("🚀 ResumeIQ v2.0")

