📄 Document Question Answering System (AI/ML Project)

This project is developed as part of the Calder AI/ML Internship selection process.

🚀 Project Overview
The Document Question Answering System allows users to extract information from a PDF document and retrieve relevant answers based on user queries.

The system processes the document, converts its content into numerical representations using Natural Language Processing (NLP), and performs similarity-based retrieval to return the most relevant text segment.

 🎯 Objective
- Extract textual content from a PDF document
- Implement keyword/similarity-based search
- Retrieve relevant answers from the document
- Handle queries with no matching content

 ✨ Features
- 📄 PDF text extraction using PyMuPDF
- 🧠 TF-IDF based text vectorization
- 📊 Cosine similarity for matching queries
- ⚡ Fast retrieval of relevant text
- ❌ Handles unknown queries using threshold logic
- 🧩 Modular and clean code structure

 🛠️ Technologies Used
- Python
- PyMuPDF (for PDF processing)
- Scikit-learn
  - TF-IDF Vectorizer
  - Cosine Similarity


## 📂 Project Structure# Document-Question-Answering-System-AI-ML-
document_qa/
│── data/
│ └── sample.pdf
│── src/
│ ├── extractor.py
│ └── qa_system.py
│── app.py
│── requirements.txt
│── README.md
