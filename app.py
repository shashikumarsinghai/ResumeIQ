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
    st.subheader("Resume Analyzer, ATS Score & Career Recommendation")

with col2:
    st.metric("Version", "2.0")

st.write(
    """
Welcome to **ResumeIQ**.

Upload your resume and let us analyze your skills, evaluate your resume, and recommend the best career opportunities based on your profile.
"""
)

st.info("📄 Upload your resume to analyze skills, calculate ATS score, and get career recommendations.")

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

    st.subheader("📄 Resume Text")

    st.text_area(
        label="Extracted Resume Text",
        value=resume_text,
        height=300
    )

    skills = extract_skills(resume_text)

#-------Skills Extraction--------

    st.subheader("🧠 Extracted Skills")

    if skills:
        for skill in skills:
            st.success(skill)
    else:
        st.warning("No skills detected.")

    score, matched_skills, missing_skills = calculate_resume_score(skills)

#-------Resume Dashboard--------

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

#-------Job Recommendations--------
    st.subheader("💼 Job Recommendations")

    jobs = recommend_jobs(skills)

    for job in jobs:
        st.info(job)

# -------Course Recommendations--------

    st.subheader("📚 Recommended Courses")

    courses = recommend_courses(missing_skills)

    if courses:
        for course in courses:
            st.info(course)

    else:
        st.success("🎉 No course recommendations. Your resume already covers all required skills!")

#-------Career Tips--------

    st.header("🎯 Career Tips")

    if score >= 80:
        st.success("Excellent Resume! Keep updating your projects and certifications.")

    elif score >= 60:
        st.warning("Good Resume! Improve missing skills to increase your ATS score.")

    else:
        st.error("Your resume needs improvement. Learn the recommended Courses and add more projects.")          

# -------Charts--------

    st.subheader("📊 Skills Analysis Chart")

    fig = skill_chart(matched_skills, missing_skills)
    
    st.pyplot(fig)

# -------Resume Feedback--------

    st.subheader("📋 Resume Feedback")

    feedback = generate_feedback(score, missing_skills)

    for item in feedback:
        st.write(item)

# -------Download PDF Report--------

    st.subheader("📄 Download Resume Report")

    pdf_file = create_pdf(score, matched_skills, missing_skills, jobs)

    with open(pdf_file, "rb") as file:
        st.download_button(
            label="Download Resume Report",
            data=file,
            file_name="Resume_Report.pdf",
            mime="application/pdf"
        )        

#--------Sidebar--------
st.sidebar.title("📋 ResumeIQ")

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

