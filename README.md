
# 🚀 AI Resume Analyzer (NLP-Based ATS System)

An end-to-end NLP-based system that analyzes resumes against job descriptions and provides a match score, extracted skills, and missing skills — simulating a real Applicant Tracking System (ATS).

---

## 🧠 Project Overview

This project allows users to:

- Upload a resume (PDF)
- Paste a job description
- Get:
  - 📊 Match Score (%)
  - 🧩 Extracted Skills
  - ❌ Missing Skills
  - 🏆 Ranking (for multiple resumes)

---

## 🏗️ Architecture

Resume (PDF) + Job Description
↓
Text Extraction
↓
Text Preprocessing (NLP)
↓
TF-IDF Vectorization
↓
Cosine Similarity
↓
Match Score + Skills + Ranking
↓
Flask API Response + UI

---

## ⚙️ Tech Stack

- **Programming Language:** Python  
- **Backend:** Flask  
- **Machine Learning:** Scikit-learn (TF-IDF, Cosine Similarity)  
- **NLP:** NLTK  
- **PDF Parsing:** pdfminer.six  
- **Frontend:** HTML, CSS, JavaScript  

---

## ✨ Features

- ✅ Resume parsing from PDF  
- ✅ NLP-based text preprocessing  
- ✅ TF-IDF + Cosine similarity matching  
- ✅ Skill extraction  
- ✅ Missing skill detection  
- ✅ Multi-resume ranking  
- ✅ Interactive UI with score visualization  

---

## 📁 Project Structure
AI-Resume-Analyzer/
│
├── app.py
├── utils/
│ ├── parser.py
│ ├── preprocess.py
│ ├── similarity.py
│ └── extractor.py
│
├── templates/
│ └── index.html
│
├── uploads/
├── requirements.txt
└── README.md



---

## 🚀 Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Pratik0718/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Download NLTK Data
python -m nltk.downloader stopwords
5️⃣ Run Application
python app.py
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Download NLTK Data
python -m nltk.downloader stopwords
5️⃣ Run Application
python app.py



1️⃣ Upload to GitHub
```bash
git init
git add .
git commit -m "AI Resume Analyzer Project"
git branch -M main
git remote add origin <your-repo-link>
git push -u origin main
=======
# AI-Resume-Analyzer-Project

