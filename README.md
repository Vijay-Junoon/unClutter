# Unclutter 🧹

An AI-powered smart document organization system designed to automatically cluster and organize files based on semantic content similarity. Unclutter extracts text from documents, generates contextual embeddings using transformer models, and groups related files using unsupervised learning techniques to reduce manual file management.

---

## 📌 Features

### 📂 Intelligent File Organization
- Automatically groups related documents into clusters
- Reduces manual sorting effort
- Organizes cluttered folders intelligently

### 🧠 Semantic Document Analysis
- Extracts textual content from documents
- Understands document meaning using transformer embeddings
- Groups files based on semantic similarity rather than keyword matching

### 🤖 AI-Based Clustering
- Uses **Sentence Transformers** for document embeddings
- Implements **DBSCAN** for unsupervised document clustering
- Handles unknown cluster counts dynamically

### 📄 PDF Text Extraction
- Extracts text from PDF documents
- Supports content-based classification
- Works with real-world document structures

### 🖥️ Modern Desktop Interface
- Clean and intuitive desktop GUI
- Built for smooth file interaction
- User-friendly workflow for organizing files

### ⚡ Automated Workflow
- Scans documents automatically
- Generates semantic vectors
- Clusters related files
- Creates organized output structure

---

## 🧠 Machine Learning Workflow

### 1. Document Loading
The system scans and loads files from selected directories.

### 2. Text Extraction
Text is extracted from PDF documents using:

```python
PyMuPDF (fitz)
```

### 3. Semantic Embedding Generation
Documents are converted into semantic vector representations using:

```python
SentenceTransformer()
```

This enables the system to understand document meaning/context instead of relying on simple keyword matching.

### 4. Document Clustering
The embeddings are clustered using:

```python
DBSCAN()
```

DBSCAN automatically groups similar documents together without requiring a predefined number of clusters.

### 5. Smart Organization
Clustered documents are grouped into meaningful folders for better file management.

---

## 🛠️ Tech Stack

### Programming Language
- Python

### Artificial Intelligence / NLP
- Sentence Transformers
- Semantic Embeddings
- Natural Language Processing (NLP)

### Machine Learning
- DBSCAN Clustering
- Scikit-learn

### File Processing
- PyMuPDF (fitz)

### GUI
- Tkinter / CustomTkinter *(or PyQt5 if migrated)*

### Data Processing
- NumPy
- Pandas

### Additional Libraries
- OS
- Pathlib
- Threading

---

## 📂 Supported Workflow

```text
Input Files
     ↓
Text Extraction
     ↓
Sentence Embeddings
     ↓
DBSCAN Clustering
     ↓
Smart Folder Organization
```

---

## 🗂️ Project Structure

```text
Unclutter/
│── root.py
│── extractData.py
│── clustering.py
│── ui.py
│── assets/
│── sample_documents/
│── requirements.txt
```

*(Update filenames based on your actual project structure.)*

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/Vijay-Junoon/unClutter.git
cd unclutter
```

### 2. Install dependencies

```bash
pip install sentence-transformers scikit-learn pymupdf customtkinter pillow pandas numpy
```

### 3. Run the Application

```bash
python unclutter.py
```

---

## 🚀 Future Improvements

- Add drag-and-drop file support
- Support additional document formats (.docx, .txt, images)
- Improve clustering accuracy using advanced embedding models
- Add cloud synchronization support
- Implement document summarization
- Introduce duplicate file detection
- Add OCR support for scanned PDFs

---

## 📈 Learning Outcomes

Through this project, I learned:

- Transformer-based NLP using **Sentence Transformers**
- Semantic similarity analysis for documents
- Unsupervised learning using **DBSCAN**
- PDF text extraction with **PyMuPDF**
- Desktop GUI development
- Real-world AI application development
- File automation and intelligent organization systems

---

## 👨‍💻 Author

**V Vijay**  
GitHub: https://github.com/Vijay-Junoon  
LinkedIn: https://linkedin.com/in/vijay-developer
