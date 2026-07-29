REQUIRED_SKILLS = [
    "Python",
    "SQL",
    "Git",
    "Machine Learning",
    "Pandas",
    "NumPy",
    "Scikit-learn",
    "TensorFlow",
    "Docker",
    "AWS"
]

def calculate_resume_score(found_skills):
    matched = []

    for skill in REQUIRED_SKILLS:
        if skill in found_skills:
            matched.append(skill)

    score = int((len(matched) / len(REQUIRED_SKILLS)) * 100)

    missing = []

    for skill in REQUIRED_SKILLS:
        if skill not in matched:
            missing.append(skill)

    return score, matched, missing