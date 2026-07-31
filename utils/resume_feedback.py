def generate_feedback(score, missing_skills):

    feedback = []

    if score >= 80:
        feedback.append("✅ Excellent resume! Your profile is strong.")
        
    elif score >= 60:
        feedback.append("👍 Good resume, but there is room for improvement.")
        
    else:
        feedback.append("⚠️ Your resume needs improvement.")

    if len(missing_skills) > 0:
        feedback.append("📚 Learn these important skills:")

        for skill in missing_skills:
            feedback.append(f". {skill}")

    feedback.append("💡 Add more projects and certifications to strengthen your resume.")

    return feedback