# 📚 Document Chat Application

## Overview
This project is a **Retrieval-Augmented Generation (RAG) application** that allows users to upload documents (**PDF, DOCX, TXT**) and ask questions based on their content. The app retrieves relevant passages using **FAISS** and generates AI-driven responses using a **T5 Transformer model**.

## Features
- **Supports Multiple File Formats:** PDF, DOCX, and TXT.
- **Text Chunking & Indexing:** Preprocesses text into smaller chunks and indexes them using FAISS.
- **Semantic Search:** Uses **SentenceTransformers** to find the most relevant document passages.
- **AI-Powered Response Generation:** Utilizes **T5 Transformer** to generate meaningful responses.
- **Interactive UI:** Built with **Streamlit** for a simple and user-friendly experience.

## Technologies Used
- **Python** (Primary programming language)
- **Streamlit** (For interactive UI)
- **FAISS** (For vector-based similarity search)
- **T5 Transformer Model** (For text generation)
- **SentenceTransformers** (For embedding document text)
- **PyPDF2** (For parsing PDF documents)
- **docx (python-docx)** (For extracting text from DOCX files)

## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-repo/document-chat-app.git
   cd document-chat-app
   ```
2. **Install dependencies:**
   ```bash
   pip install streamlit transformers faiss-cpu sentence-transformers PyPDF2 python-docx numpy
   ```
3. **Run the application:**
   ```bash
   streamlit run rag_app.py
   ```

## How It Works
1. **Upload Documents:** Users can upload multiple PDF, DOCX, or TXT files.
2. **Processing & Indexing:**
   - Extracts text from uploaded files.
   - Splits text into chunks.
   - Embeds and indexes chunks using FAISS.
3. **Ask Questions:** Users enter queries, and the system:
   - Finds the most relevant document passages.
   - Generates AI-based responses using the **T5 model**.
4. **Results Displayed:** The app shows AI-generated answers and relevant text excerpts.

## Future Improvements
- Add support for **more document formats** (e.g., Excel, PPTX).
- Improve text chunking strategy for better context retrieval.
- Optimize model response generation with **larger T5 variants**.
- Implement **real-time indexing** for dynamically added documents.

## License
This project is open-source and available under the **MIT License**.

---

🚀 **Try out the Document Chat App and transform how you interact with documents using AI!**

