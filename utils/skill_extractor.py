SKILLS = [
    "Python",
    "C++",
    "Java",
    "SQL",
    "HTML",
    "CSS",
    "JavaScript",
    "Git",
    "GitHub",
    "Machine Learning",
    "Deep Learning",
    "Data Science",
    "Pandas",
    "NumPy",
    "Matplotlib",
    "Scikit-learn",
    "TensorFlow",
    "PyTorch",
    "Flask",
    "Django",
    "Streamlit"
]

def extract_skills(resume_text):
    found_skills = []

    text = resume_text.lower()

    for skill in SKILLS:
        if skill.lower() in text:
            found_skills.append(skill)

    return found_skills
