import streamlit as st
import matplotlib.pyplot as plt

from parser import *
from helper import (
    advanced_score,
    ai_feedback,
    skill_match,
    career_recommendation,
    skill_gap,
    interview_questions
)

st.set_page_config(
    page_title="AI Career Intelligence System",
    layout="wide"
)

# ================= HEADER =================

st.title("🚀 AI Career Intelligence System")
st.write("Resume Analysis + Career Guidance + Skill Gap Detection")

st.markdown("---")

# ================= INPUT =================

uploaded_file = st.file_uploader(
    "📄 Upload Resume PDF"
)

job_desc = st.text_area(
    "💼 Paste Job Description (Optional)"
)

# ================= MAIN =================

if uploaded_file:

    text = extract_text(uploaded_file)

    email = extract_email(text)
    phone = extract_phone(text)
    skills = extract_skills(text)

    score = advanced_score(text, skills)

    career = career_recommendation(skills)

    # ================= TOP METRICS =================

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("📧 Email", email)

    with col2:
        st.metric("📞 Phone", phone)

    with col3:
        st.metric("📊 Score", f"{score}/100")

    st.markdown("---")

    # ================= CAREER =================

    st.subheader("🎯 Recommended Career")

    st.success(career)

    st.markdown("---")

    # ================= STRENGTH METER =================

    st.subheader("💪 Resume Strength")

    st.progress(score / 100)

    st.markdown("---")

    # ================= RANK =================

    if score >= 80:
        rank = "A+"

    elif score >= 60:
        rank = "A"

    elif score >= 40:
        rank = "B"

    else:
        rank = "C"

    st.subheader("🏆 Resume Rank")
    st.success(rank)

    st.markdown("---")

    # ================= SKILLS =================

    st.subheader("📌 Extracted Skills")

    st.write(", ".join(skills))

    st.markdown("---")

    # ================= JOB MATCH =================

    if job_desc:

        st.subheader("🔍 Skill Match")

        match = skill_match(
            text,
            job_desc,
            skills
        )

        for k, v in match.items():
            st.write(f"{k} → {v}")

        st.markdown("---")

        # ================= GAP ANALYSIS =================

        gaps = skill_gap(
            job_desc,
            skills
        )

        st.subheader("🚨 Missing Skills")

        if gaps:

            for g in gaps:
                st.error(g)

        else:
            st.success("No major skill gaps detected")

        st.markdown("---")

    # ================= FEEDBACK =================

    st.subheader("🧠 AI Suggestions")

    feedback = ai_feedback(
        text,
        skills
    )

    for f in feedback:
        st.warning(f)

    st.markdown("---")

    # ================= INTERVIEW QUESTIONS =================

    st.subheader("🎤 Interview Questions")

    questions = interview_questions(
        career
    )

    for q in questions:
        st.info(q)

    st.markdown("---")

    # ================= GRAPH =================

    if skills:

        st.subheader("📊 Skill Graph")

        fig, ax = plt.subplots()

        ax.bar(
            skills,
            [1] * len(skills)
        )

        plt.xticks(rotation=45)

        st.pyplot(fig)

    st.markdown("---")

    st.success("✅ Resume Analysis Completed")