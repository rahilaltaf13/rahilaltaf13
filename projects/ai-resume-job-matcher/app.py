import re
from pathlib import Path

import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

try:
    from pypdf import PdfReader
except ImportError:
    PdfReader = None

try:
    from docx import Document
except ImportError:
    Document = None

SKILLS = [
    "python", "sql", "excel", "power bi", "tableau", "pandas", "numpy",
    "scikit-learn", "machine learning", "deep learning", "nlp",
    "generative ai", "llm", "rag", "streamlit", "tensorflow", "pytorch",
    "data analysis", "data visualization", "statistics", "git", "github",
    "rest api", "fastapi", "flask", "aws", "azure", "docker",
    "arduino", "robotics", "ros", "solidworks", "matlab"
]

def read_resume(uploaded_file):
    name = uploaded_file.name.lower()
    if name.endswith(".txt"):
        return uploaded_file.getvalue().decode("utf-8", errors="ignore")
    if name.endswith(".pdf"):
        if PdfReader is None:
            raise RuntimeError("Install pypdf to read PDF files.")
        reader = PdfReader(uploaded_file)
        return "\n".join(page.extract_text() or "" for page in reader.pages)
    if name.endswith(".docx"):
        if Document is None:
            raise RuntimeError("Install python-docx to read DOCX files.")
        doc = Document(uploaded_file)
        return "\n".join(p.text for p in doc.paragraphs)
    raise ValueError("Supported formats: PDF, DOCX, TXT")

def normalize(text):
    return re.sub(r"\s+", " ", text.lower()).strip()

def find_skills(text):
    normalized = normalize(text)
    return sorted({skill for skill in SKILLS if skill in normalized})

def calculate_match(resume_text, job_text):
    vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2))
    matrix = vectorizer.fit_transform([resume_text, job_text])
    score = float(cosine_similarity(matrix[0:1], matrix[1:2])[0][0]) * 100
    resume_skills = set(find_skills(resume_text))
    job_skills = set(find_skills(job_text))
    matched = sorted(resume_skills & job_skills)
    missing = sorted(job_skills - resume_skills)
    return score, matched, missing, sorted(job_skills)

st.set_page_config(page_title="AI Resume & Job Matcher", page_icon="🎯", layout="wide")
st.title("🎯 AI Resume & Job Matcher")
st.caption("A local-first portfolio MVP that compares resume text with a job description.")

with st.sidebar:
    st.header("How it works")
    st.write("1. Upload a resume (PDF, DOCX, or TXT).")
    st.write("2. Paste a job description.")
    st.write("3. Review similarity, skill overlap, and suggested gaps.")
    st.info("Your resume is processed in this app session and is not sent to an external AI service.")

col1, col2 = st.columns(2)
with col1:
    resume_file = st.file_uploader("Upload your resume", type=["pdf", "docx", "txt"])
with col2:
    job_text = st.text_area("Paste the job description", height=260, placeholder="Paste the full job description here...")

if st.button("Analyze match", type="primary", use_container_width=True):
    if not resume_file or not job_text.strip():
        st.warning("Upload a resume and paste a job description first.")
    else:
        try:
            resume_text = read_resume(resume_file)
            if len(resume_text.strip()) < 40:
                st.error("Not enough readable text was extracted. Try a text-based PDF or DOCX.")
            else:
                score, matched, missing, job_skills = calculate_match(resume_text, job_text)
                st.subheader("Results")
                a, b, c = st.columns(3)
                a.metric("Text similarity", f"{score:.1f}%")
                b.metric("Skills found in job description", len(job_skills))
                c.metric("Matched skills", len(matched))
                st.progress(min(score / 100, 1.0))
                left, right = st.columns(2)
                with left:
                    st.markdown("#### Skills detected in both")
                    if matched:
                        st.success(" · ".join(matched))
                    else:
                        st.write("No overlap detected from the built-in skill list.")
                with right:
                    st.markdown("#### Skills to consider developing")
                    if missing:
                        st.warning(" · ".join(missing))
                    else:
                        st.success("All detected job skills appear in the resume.")
                st.markdown("#### Job-description skills detected")
                st.write(" · ".join(job_skills) if job_skills else "No listed skills detected.")
                st.caption("This is a heuristic screening aid, not a hiring decision or a guarantee of interview selection. Similarity is based on TF-IDF text overlap, not semantic understanding.")
        except Exception as exc:
            st.error(f"Could not analyze the files: {exc}")
