def advanced_score(text, skills):
    score = 0

    if len(text) > 1500:
        score += 25

    if len(skills) >= 3:
        score += 25
    elif len(skills) >= 1:
        score += 10

    if "project" in text.lower():
        score += 20

    if "experience" in text.lower():
        score += 20

    if "certificate" in text.lower():
        score += 10

    return min(score, 100)


def ai_feedback(text, skills):
    feedback = []

    if len(skills) < 3:
        feedback.append("Add more technical skills")

    if "project" not in text.lower():
        feedback.append("Add projects")

    if "experience" not in text.lower():
        feedback.append("Add experience/internship")

    if len(text) < 1000:
        feedback.append("Resume is too short")

    if not feedback:
        feedback.append("Excellent Resume")

    return feedback


def skill_match(text, job_desc, skills):
    if not job_desc:
        return {}

    result = {}

    for s in skills:
        if s.lower() in job_desc.lower():
            result[s] = "Matched ✔"
        else:
            result[s] = "Not Matched ✘"

    return result


def career_recommendation(skills):

    skills = [s.lower() for s in skills]

    if "python" in skills and "sql" in skills:
        return "Data Analyst"

    elif "machine learning" in skills:
        return "ML Engineer"

    elif "html" in skills and "css" in skills:
        return "Web Developer"

    else:
        return "Software Developer"


def skill_gap(job_desc, skills):

    important = [
        "python",
        "sql",
        "aws",
        "docker",
        "power bi"
    ]

    missing = []

    for skill in important:
        if skill in job_desc.lower() and skill not in [s.lower() for s in skills]:
            missing.append(skill)

    return missing


def interview_questions(role):

    questions = {
        "Data Analyst": [
            "What is SQL Join?",
            "What is Pandas?",
            "Explain Data Cleaning."
        ],

        "ML Engineer": [
            "What is Overfitting?",
            "Difference between CNN and RNN?",
            "Explain Cross Validation."
        ],

        "Web Developer": [
            "What is DOM?",
            "Difference between GET and POST?",
            "What is Responsive Design?"
        ]
    }

    return questions.get(
        role,
        ["Tell me about yourself"]
    )