def recommend_jobs(skills):

    jobs = []

    skills = set(skills)

    if {"python", "Machine learning"} <= skills:
        jobs.append("AI/ML Engineer")

    if {"python", "SQL", "pandas"} <= skills:
        jobs.append("Data Analyst")

    if {"python", "Flask"} <= skills:
        jobs.append("Python Developer")

    if {"python", "TensorFlow"} <= skills:
        jobs.append("Deep Learning Engineer")

    if {"python", "Scikit-learn"} <= skills:
        jobs.append("Machine Learning Engineer")

    if not jobs:
        jobs.append("No suitable job found. Learn more skills!")

    return jobs       