from app import find_skills, normalize

def test_normalize_collapses_whitespace():
    assert normalize(" Python  SQL\n") == "python sql"

def test_find_skills_detects_known_terms():
    skills = find_skills("I use Python, SQL, and Power BI for data analysis.")
    assert "python" in skills
    assert "sql" in skills
    assert "power bi" in skills
