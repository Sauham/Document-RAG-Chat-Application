# Document RAG Chat Application

## Overview
The **Document RAG Chat Application** is an advanced chatbot powered by Retrieval-Augmented Generation (RAG). It enables users to upload documents, retrieve relevant information, and interact with an AI-powered chatbot that provides context-aware responses based on the uploaded data.

## Features
- **Document Uploading**: Users can upload PDF, DOCX, or TXT files.
- **Retrieval-Augmented Generation (RAG)**: Enhances responses with document-based retrieval.
- **AI-Powered Chatbot**: Provides context-aware responses.
- **Efficient Query Handling**: Uses embeddings and vector databases for fast retrieval.
- **User-Friendly Interface**: Built with a clean and interactive UI.

## Tech Stack
- **Backend**: Python, FastAPI/Flask
- **Frontend**: React.js / Streamlit (optional)
- **Database**: FAISS / ChromaDB / Pinecone
- **LLM**: OpenAI GPT / LlamaIndex / LangChain

## Installation
### Prerequisites
Ensure you have the following installed:
- Python (>= 3.8)
- Node.js (if using React frontend)
- Virtual environment (optional but recommended)

### Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/Sauham/Document-RAG-Chat-Application.git
   cd Document-RAG-Chat-Application
   ```

2. **Create Virtual Environment & Install Dependencies**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Run the Backend**
   ```bash
   python app.py  # Or uvicorn main:app --reload (if using FastAPI)
   ```

4. **Run the Frontend (if applicable)**
   ```bash
   cd frontend
   npm install
   npm start
   ```

## Usage
1. Open the application in your browser.
2. Upload a document (PDF, DOCX, TXT).
3. Ask questions related to the uploaded document.
4. Get AI-powered responses with relevant context.

## Future Enhancements
- Add support for multiple document uploads.
- Implement authentication for user sessions.
- Improve response accuracy with better fine-tuned models.

## Contributing
Contributions are welcome! Feel free to fork the repository, create a feature branch, and submit a pull request.

## License
This project is licensed under the MIT License.

---
Feel free to reach out with any questions or suggestions!
