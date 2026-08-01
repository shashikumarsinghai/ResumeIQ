COURSES = {
    "Python": [
        "Python for Everybody - Coursera",
        "Python Full Course - freeCodeCamp",
    ],
    "SQL" : [
        "SQL for Data Science - Coursera",
        "SQL Tutorial - W3Schools",
    ],
    "Git": [
        "Git & GitHub - freeCodeCamp",
        "Git Complete Course - Youtube",
    ],
    "Machine Learning": [
        "Machine Learning - Andrew Ng",
        "Machine Learning Crash Course - Google",
    ],
    "Pandas": [
        "Data Analysis with Pandas - freeCodeCamp",
        "Pandas Course - Kaggle Learn",
    ],
    "NumPy": [
        "NumPy Tutorial - freeCodeCamp",
        "NumPy Course - Kaggle Learn",
    ],
    "Scikit-learn": [
        "Machine Learning with Scikit-learn - freeCodeCamp",
        "Scikit-learn Documentation - Official",
    ],
    "TensorFlow": [
        "Deep Learning with TensorFlow - Coursera",
        "TensorFlow 2.0 Complete Course - freeCodeCamp",
    ],
    "Docker": [
        "Docker Crash Course",
        "Docker Complete Course - Youtube",
    ],
    "AWS": [
        "AWS Cloud Practitioner Essentials",
        "AWS Fundamentals - Coursera",
    ]
}

def recommend_courses(missing_skills):
    recommended_courses = []

    for skill in missing_skills:
        if skill in COURSES:
            recommended_courses.extend(COURSES[skill])

    return recommended_courses