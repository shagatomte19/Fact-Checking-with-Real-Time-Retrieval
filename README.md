# Fact-Checking-with-Real-Time-Retrieval


# 🔍 Automated Fact-Checking System with Real-Time Evidence Retrieval  

## 📌 Overview  
This project is an **AI-powered fact-checking system** that verifies claims by retrieving evidence from **verified sources** such as **scientific papers, government reports, and fact-checking databases (Snopes, FEVER, etc.)**.  

🚀 **Key Features:**  
- **Real-Time Data Ingestion**: Scrapes fact-checking sources & monitors live news feeds (RSS/Twitter API).  
- **Retrieval-Augmented Generation (RAG)**: Uses **LlamaIndex + Pinecone/FAISS** for vector-based evidence retrieval.  
- **Claim Verification Model**: Fine-tuned **Mistral-7B** model classifies claims as **True/False** with evidence.  
- **Human-Readable Explanations**: **GPT-4** generates explanations with citations.  
- **MLOps Integration**: Tracks performance with **Weights & Biases (W&B)** & detects bias using **Fairlearn**.  
- **API & UI**: **FastAPI backend** + lightweight **React/Next.js frontend** (deployed on **Vercel**).  

---

## 🏗️ Project Architecture  

```plaintext
fact-checking-system/
│── data_pipeline/
│   ├── ingest_news.py  
│   ├── ingest_fever.py  
│   ├── preprocess.py  
│── model/
│   ├── train_mistral.py  
│   ├── evaluate.py  
│   ├── export.py  
│── retriever/
│   ├── index_documents.py  
│   ├── retrieve.py  
│── api/
│   ├── main.py  
│   ├── inference.py  
│── frontend/
│   ├── pages/  
│   ├── styles/  
│── evaluation/
│   ├── bias_detection.py  
│   ├── monitoring.py  
│── deployment/
│   ├── Dockerfile  
│   ├── kubernetes.yaml  
│── .github/workflows/
│   ├── ci_cd.yml  
│── notebooks/
│   ├── experimentation.ipynb  
│── .gitignore
│── requirements.txt
│── README.md
```

---

## 📚 Data Sources  

🔹 **Fact-Checking Databases**:  
- [FEVER Dataset](https://fever.ai/) (Fact Extraction & Verification)  
- [Snopes](https://www.snopes.com/) (Scraped Fact Checks)  
- [Politifact](https://www.politifact.com/) (Manually Extracted Labeled Claims)  

🔹 **Real-Time News Sources**:  
- **RSS Feeds**: Google News, BBC, Reuters  
- **Twitter API**: Tracks trending misinformation topics  
- **ArXiv API**: Retrieves scientific papers for technical claims  

---

## 🚀 Tech Stack  

| Component | Technology Used |
|-----------|----------------|
| **Backend API** | FastAPI |
| **Model Training** | PyTorch, Hugging Face Transformers |
| **Claim Verification Model** | Fine-tuned Mistral-7B |
| **Evidence Retrieval** | LlamaIndex + FAISS/Pinecone |
| **Response Generation** | GPT-4 (via OpenAI API) |
| **MLOps & Monitoring** | Weights & Biases (W&B), Fairlearn |
| **UI** | React/Next.js (deployed on Vercel) |
| **CI/CD** | GitHub Actions |
| **Deployment** | Railway.app / Render (Backend), Vercel (Frontend) |

---

## 🛠️ Installation  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/your-username/fact-checking-system.git
cd fact-checking-system
```

### **2️⃣ Set Up the Backend (FastAPI)**
#### ➤ Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
```
#### ➤ Install Dependencies
```bash
pip install -r requirements.txt
```
#### ➤ Run FastAPI Server
```bash
uvicorn api.main:app --reload
```
➡ The API will be available at: **http://127.0.0.1:8000**

---


## 📝 Contributing  
🙌 Contributions are welcome! If you’d like to improve this project, feel free to:  
1. Fork the repository  
2. Create a feature branch (`git checkout -b feature-name`)  
3. Commit your changes (`git commit -m "Add new feature"`)  
4. Push to your branch (`git push origin feature-name`)  
5. Create a Pull Request  

---

## 📜 License  
This project is **open-source** under the **MIT License**.  

```
Yours,
Enamul Hasan Shagato
