# 🔍 VAPORTRACE // Advanced Document Forensics & Semantic Reasoning Engine

> **VAPORTRACE** is an AI-powered document forensics platform that detects semantic manipulation, entity tampering, and structural inconsistencies between a trusted baseline document and a questioned version. By combining Natural Language Processing, Machine Learning, and interactive graph visualization, it provides an explainable forensic analysis instead of simple text comparison.

---

## 🚀 Overview

Traditional document comparison tools focus primarily on exact text differences. However, malicious edits often involve subtle wording changes, entity replacements, or contextual manipulation that preserve grammar while altering meaning.

**VAPORTRACE** addresses this challenge by analyzing documents at a semantic level. It measures contextual similarity using sentence embeddings, tracks Named Entity changes, and generates an explainable forensic report with an interactive relationship graph.

The platform is designed for educational research, AI experimentation, cybersecurity demonstrations, and document integrity analysis.

---

# ✨ Features

### 🧠 Semantic Drift Detection

Uses transformer-based sentence embeddings to measure contextual similarity between corresponding paragraphs instead of relying solely on keyword matching.

- Detects rewritten content
- Identifies paraphrased manipulation
- Computes semantic similarity scores
- Highlights meaning changes despite identical vocabulary

---

### 🏷️ Entity Tampering Detection

Named Entity Recognition (NER) identifies critical entities and compares them between documents.

Supported entities include:

- 👤 Persons
- 🏢 Organizations
- 📍 Locations
- 📅 Dates
- 💰 Money
- 🌐 Geopolitical Entities
- 📦 Products

The engine automatically flags:

- Entity insertion
- Entity removal
- Entity replacement
- Suspicious substitutions

---

### 📄 Intelligent Document Parsing

Documents are parsed while preserving logical structure.

Supports:

- Raw text
- PDF documents
- Byte streams

Powered by **PyMuPDF**, ensuring accurate extraction before analysis.

---

### 🤖 AI Reasoning Engine

Rather than presenting raw similarity scores, the reasoning module interprets findings and produces automated forensic observations.

Example:

> Paragraph 5 exhibits significant semantic drift (Similarity: 41%). The organization entity has changed from **OpenAI** to **Open Data Institute**, suggesting possible contextual manipulation.

---

### 🌐 Interactive Network Visualization

Every analysis is represented as a directed graph.

The graph visualizes:

- Document hierarchy
- Paragraph relationships
- Semantic links
- Entity modifications
- Suspicious nodes
- Confidence levels

Built using **Vis.js** for an interactive forensic experience.

---

# 🏗️ System Architecture

```
                    Baseline Document
                           │
                           ▼
                  Document Parser
                    (PyMuPDF)
                           │
                           ▼
                 Sentence Segmentation
                           │
        ┌──────────────────┴──────────────────┐
        ▼                                     ▼
 Semantic Embedding Engine             Named Entity Engine
(sentence-transformers)                    (spaCy)
        │                                     │
        └──────────────┬──────────────────────┘
                       ▼
              Semantic Comparison
                       │
                       ▼
              AI Reasoning Engine
                       │
                       ▼
              Forensic Report Generator
                       │
                       ▼
          Interactive Network Graph (Vis.js)
```

---

# ⚙️ Technology Stack

## Backend

- Python
- Flask
- NumPy
- scikit-learn

---

## Artificial Intelligence

- sentence-transformers
- all-MiniLM-L6-v2
- spaCy

---

## Document Processing

- PyMuPDF (fitz)

---

## Frontend

- HTML5
- CSS3
- Vanilla JavaScript
- Vis.js

---

# 📂 Project Structure

```
VAPORTRACE/
│
├── app.py
├── requirements.txt
├── README.md
│
├── static/
│   ├── css/
│   ├── js/
│   └── assets/
│
├── templates/
│   └── index.html
│
├── uploads/
│
├── models/
│
└── utils/
    ├── parser.py
    ├── semantic_engine.py
    ├── entity_engine.py
    ├── reasoning.py
    └── graph.py
```

---

# 🛠️ Installation

## Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/VAPORTRACE.git
cd VAPORTRACE
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Download spaCy Model

```bash
python -m spacy download en_core_web_sm
```

---

## Run the Application

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

# 🔬 Analysis Pipeline

```
Input Documents
       │
       ▼
Document Parsing
       │
       ▼
Sentence Extraction
       │
       ▼
Sentence Embedding Generation
       │
       ▼
Semantic Similarity Analysis
       │
       ▼
Named Entity Extraction
       │
       ▼
Entity Drift Detection
       │
       ▼
Reasoning Engine
       │
       ▼
Forensic Report
       │
       ▼
Interactive Network Visualization
```

---

# 📊 Example Output

```
Document Similarity
──────────────────────────

Overall Semantic Score
92.41%

Paragraph Analysis

Paragraph 2
Similarity: 97%

Paragraph 3
Similarity: 44%
⚠ High Semantic Drift

Entity Analysis

Original:
OpenAI

Modified:
OpenAI Research Labs

Status:
Entity Injection Detected

Reasoning

The paragraph preserves grammatical structure while introducing a new organization entity that changes the contextual interpretation of the document.
```

---

# 🎯 Use Cases

- 📑 Document Integrity Verification
- 🛡️ Digital Forensics
- 📚 Academic Plagiarism Research
- 📰 News Authenticity Analysis
- ⚖️ Legal Document Comparison
- 🏛 Contract Revision Tracking
- 🔒 Cybersecurity Demonstrations
- 🤖 NLP Research Projects

---

# 📈 Future Enhancements

- Multi-language support
- OCR for scanned documents
- Knowledge Graph integration
- Explainable AI confidence scoring
- PDF forensic timeline
- Batch document comparison
- LLM-powered reasoning summaries
- Exportable forensic reports (PDF)

---

# 🤝 Contributing

Contributions are welcome!

If you would like to improve VAPORTRACE:

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature/new-feature
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push your branch

```bash
git push origin feature/new-feature
```

5. Open a Pull Request

---
