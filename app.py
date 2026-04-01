from flask import Flask, request, jsonify, render_template
import os

from utils.parser import extract_resume_text
from utils.preprocess import clean_text
from utils.similarity import calculate_similarity
from utils.extractor import extract_skills

app = Flask(__name__)

# 📁 Upload folder
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# 🏠 Home route
@app.route('/')
def home():
    return render_template('index.html')


# 🧠 Missing skills logic
def missing_skills(resume_skills, jd_text):
    skills_list = [
        "python", "machine learning", "deep learning",
        "sql", "flask", "django", "tensorflow",
        "pandas", "numpy", "data analysis"
    ]

    missing = []
    for skill in skills_list:
        if skill in jd_text and skill not in resume_skills:
            missing.append(skill)

    return missing


# 🔍 Analyze Resume
@app.route('/analyze', methods=['POST'])
def analyze():
    resume_file = request.files['resume']
    job_desc = request.form['job_desc']

    # Save file
    file_path = os.path.join(UPLOAD_FOLDER, resume_file.filename)
    resume_file.save(file_path)

    # Extract text
    resume_text = extract_resume_text(file_path)

    # Clean text
    clean_resume = clean_text(resume_text)
    clean_jd = clean_text(job_desc)

    # Similarity
    score = calculate_similarity(clean_resume, clean_jd)

    # Skills
    skills = extract_skills(clean_resume)

    # Missing skills
    missing = missing_skills(skills, clean_jd)

    return jsonify({
        "match_score": score,
        "skills": skills,
        "missing_skills": missing
    })


# 🏆 Rank multiple resumes
@app.route('/rank', methods=['POST'])
def rank():
    resumes = request.files.getlist('resumes')
    job_desc = request.form['job_desc']

    results = []

    for file in resumes:
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        text = extract_resume_text(file_path)
        clean_res = clean_text(text)
        clean_jd = clean_text(job_desc)

        score = calculate_similarity(clean_res, clean_jd)

        results.append({
            "name": file.filename,
            "score": score
        })

    results = sorted(results, key=lambda x: x['score'], reverse=True)

    return jsonify(results)


# ▶️ Run app
if __name__ == '__main__':
    app.run(debug=True)