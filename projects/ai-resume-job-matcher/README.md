# AI Resume & Job Matcher

A Python + Streamlit application that compares a resume with a job description and reports text similarity, detected skill overlap, and potential skill gaps.

## Features
- Upload resumes in PDF, DOCX, or TXT format
- Paste a job description
- TF-IDF cosine similarity score
- Rule-based skill extraction and overlap analysis
- Runs locally; no external AI API or resume upload service
- Clear limitations and transparent scoring

## Tech Stack
Python, Streamlit, scikit-learn, TF-IDF, cosine similarity, pypdf, python-docx.

## Run locally
```bash
python -m venv .venv
```

Activate the environment:

**Windows**
```bash
.venv\Scripts\activate
```

**macOS/Linux**
```bash
source .venv/bin/activate
```

Install and launch:
```bash
pip install -r requirements.txt
streamlit run app.py
```

## How it works
1. Extract text from the uploaded resume.
2. Vectorize resume and job description using TF-IDF (unigrams and bigrams).
3. Compute cosine similarity as a text-overlap indicator.
4. Detect skills using a transparent, editable skill dictionary.
5. Show matched and missing detected skills.

## Limitations
- Similarity is not a true hiring probability.
- Skill detection uses a predefined list and may miss synonyms or context.
- The tool does not evaluate experience quality, project depth, or candidate suitability.
- Scanned PDFs may require OCR, which is not included in this MVP.

## Roadmap
- Add semantic embeddings for meaning-based matching
- Add editable skill taxonomy and synonym mapping
- Add resume section extraction and explainable recommendations
- Add automated tests and sample anonymized data
- Deploy a demo with privacy-conscious handling

## Portfolio note
This is an educational portfolio project. It should not be used as the sole basis for hiring decisions.
