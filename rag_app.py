import streamlit as st
from transformers import T5ForConditionalGeneration, T5Tokenizer
import PyPDF2
from docx import Document
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Initialize SentenceTransformer for embeddings
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

# Initialize T5 model and tokenizer for response generation
tokenizer = T5Tokenizer.from_pretrained("t5-small")
model = T5ForConditionalGeneration.from_pretrained("t5-small")

# Function to parse PDFs
def parse_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = "".join([page.extract_text() for page in pdf_reader.pages if page.extract_text()])
    return text

# Function to parse DOCX files
def parse_docx(file):
    doc = Document(file)
    return "\n".join([paragraph.text for paragraph in doc.paragraphs])

# Function to parse TXT files
def parse_txt(file):
    return file.read().decode("utf-8")

# Function to preprocess text into smaller chunks
def preprocess_text(text, chunk_size=500):
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

# Function to build a FAISS index
def build_faiss_index(text_chunks):
    embeddings = embedding_model.encode(text_chunks)
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    return index, embeddings

# Function to retrieve relevant passages
def retrieve_passages(query, index, embeddings, text_chunks, top_k=3):
    query_embedding = embedding_model.encode([query])
    distances, indices = index.search(query_embedding, top_k)
    return [text_chunks[i] for i in indices[0]]

# Function to generate response using T5
def generate_response(query, relevant_passages):
    context = " ".join(relevant_passages)
    input_text = f"question: {query} context: {context}"
    input_ids = tokenizer(input_text, return_tensors="pt").input_ids
    outputs = model.generate(input_ids)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

# Streamlit App
def main():
    st.title("📚 Document Chat Application")
    st.write("Upload documents (PDF, DOCX, TXT) and ask questions!")

    # File uploader
    uploaded_files = st.file_uploader("Upload documents", type=["pdf", "docx", "txt"], accept_multiple_files=True)
    text_chunks = []

    if uploaded_files:
        for file in uploaded_files:
            if file.type == "application/pdf":
                text = parse_pdf(file)
            elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                text = parse_docx(file)
            elif file.type == "text/plain":
                text = parse_txt(file)
            text_chunks.extend(preprocess_text(text))

        # Build FAISS index
        index, embeddings = build_faiss_index(text_chunks)

        # Chat Interface
        st.write("### Chat with your documents")
        query = st.text_input("Enter your question:")

        if query:
            # Retrieve relevant passages
            relevant_passages = retrieve_passages(query, index, embeddings, text_chunks)
            # Generate response
            response = generate_response(query, relevant_passages)
            st.write("**🤖 Response:**", response)

            st.write("**📖 Relevant Passages:**")
            for passage in relevant_passages:
                st.write(passage)

# Run the Streamlit app
if __name__ == "__main__":
    main()