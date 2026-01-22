# Question Generation System (FastAPI + T5)

## 📌 Project Overview

This project is an **automatic question generation system** built using **FastAPI** and a **fine-tuned T5 transformer model**.
It accepts a textual summary as input and generates **high-quality academic questions** relevant to the content.

The system is designed for use in:

* Learning Management Systems (LMS)
* Question bank generation
* Educational content creation
* Exam preparation tools

Only **questions** are generated (no answers), with the number of questions **automatically determined based on the length of the summary**.

---

## ✨ Key Features

* Automatic question generation from summaries
* Adaptive number of questions based on text length
* High-quality, academic-style questions
* No MCQs, no repetitive answers
* Fast generation with optimized retry logic
* Export questions to **DOCX** format

---

## 🧠 Model Information

The question generation model is a **fine-tuned T5 transformer**, trained on:

* SQuAD dataset
* RACE dataset
* Additional QA-style corpora

The trained model is hosted externally due to size constraints.

### 🔗 Download Model

Download the model from Google Drive:

<https://drive.google.com/file/d/13KRQEW-sgTMXuPr9c6MeTWKIVNkdvK3i/view?usp=sharing>

After downloading, extract the folder and place it inside the project root as:

```
QNA_finetuned_model/
```

---

## 🗂️ Project Structure

```
project/
│
├── app.py                # FastAPI application
├── model_loader.py       # Loads tokenizer and model
├── qa_generator.py       # Core question generation logic
│
├── templates/
│   └── index.html        # Frontend template
│
├── static/
│   └── style.css         # UI styling
│
├── QNA_finetuned_model/  # (Downloaded separately)
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Create Virtual Environment (recommended)

```bash
python -m venv venv
venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install fastapi uvicorn transformers torch python-docx jinja2
```

### 3. Download and Place Model

* Download model from the provided Google Drive link
* Extract into:

```
QNA_finetuned_model/
```

---

## ▶️ Running the Application

Start the FastAPI server using:

```bash
uvicorn app:app --reload
```

Then open in browser:

```
http://127.0.0.1:8000
```

---

## 📝 How It Works

1. User enters a textual summary
2. System splits the text into meaningful sentences
3. Model generates questions from selected sentences
4. Number of questions is chosen automatically based on summary length
5. Questions are displayed and can be exported to DOCX

---

## 📊 Auto Question Scaling

| Summary Length | Questions Generated |
| -------------- | ------------------- |
| < 150 words    | 4 questions         |
| 150–300 words  | 6 questions         |
| 300–600 words  | 10 questions        |
| > 600 words    | 14 questions        |

---

## 🛡️ Notes

* Model files are not included in this repository
* Generated documents are temporary and not stored permanently
* System is optimized for **quality-first generation**

---

## 🎓 Academic Use

This project is suitable for:

* Final year projects
* NLP demonstrations
* Educational technology prototypes
* Research in automatic question generation

---

## 👤 Author

**Sanskar Rastogi**
Computer Science / Artificial Intelligence

---

## 📜 License

This project is for academic and educational use only.

