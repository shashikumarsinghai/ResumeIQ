import streamlit as st
import pdfplumber

st.set_page_config(
    page_title="ResumeIQ-AI",
    page_icon=":robot:",
    layout="wide"
)

st.title("🤖 ResumeIQ-AI")
st.subheader("AI-Powered Resume Analyzer & Career Recommendation System")

st.write(
    """
Welcome to **ResumeIQ-AI**.

Upload your resume and let AI analyze your skills, evaluate your resume, and recommend the best career opportunities based on your profile.
"""
)

st.divider()

st.header("🚀 Features")

st.markdown(""""
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