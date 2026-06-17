import pdfplumber
import re
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# AI model
model = SentenceTransformer("all-MiniLM-L6-v2")


# PDF TO TEXT
def extract_text(pdf_file):
    text = ""

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""

    return text


# EMAIL EXTRACTION
def extract_email(text):
    match = re.findall(r"\S+@\S+", text)
    return match[0] if match else "Not Found"


# PHONE EXTRACTION
def extract_phone(text):
    match = re.findall(r"\d{10}", text)
    return match[0] if match else "Not Found"


# SKILLS EXTRACTION
def extract_skills(text):

    skills = [
        "python",
        "java",
        "sql",
        "machine learning",
        "deep learning",
        "nlp",
        "excel",
        "pandas",
        "django",
        "flask",
        "react"
    ]

    return [s for s in skills if s in text.lower()]


# ROLE PREDICTION
def predict_role(text):

    text = text.lower()

    ml = [
        "machine learning",
        "ai",
        "deep learning",
        "nlp",
        "pytorch",
        "tensorflow"
    ]

    data = [
        "data",
        "sql",
        "pandas",
        "numpy",
        "analytics",
        "power bi"
    ]

    dev = [
        "django",
        "flask",
        "react",
        "node",
        "api",
        "backend",
        "frontend"
    ]

    if any(i in text for i in ml):
        return "ML / AI Engineer"

    elif any(i in text for i in data):
        return "Data Analyst / Data Scientist"

    elif any(i in text for i in dev):
        return "Software / Full Stack Developer"

    else:
        return "General Software Engineer"


# BASIC RESUME SCORE
def resume_score(text, skills):

    score = 0

    if extract_email(text) != "Not Found":
        score += 20

    if extract_phone(text) != "Not Found":
        score += 20

    if len(skills) >= 3:
        score += 30

    if len(text) > 1200:
        score += 30

    return min(score, 100)


# AI JOB MATCH
def match_job(resume_text, job_text):

    emb1 = model.encode(resume_text)
    emb2 = model.encode(job_text)

    score = cosine_similarity(
        [emb1],
        [emb2]
    )[0][0]

    return round(score * 100, 2)