#!/usr/bin/env python
# coding: utf-8

# Importing required libraries
import streamlit as st  # Web UI framework

from PyPDF2 import PdfReader  # For reading PDF content

from langchain.text_splitter import RecursiveCharacterTextSplitter  # To split large text into chunks
from langchain.vectorstores import FAISS  # For storing and searching vector embeddings
from langchain.embeddings.openai import OpenAIEmbeddings  # OpenAI-based embedding model
from langchain.chains.question_answering import load_qa_chain  # To load a question-answering chain
from langchain.chat_models import ChatOpenAI  # Chat model like gpt-3.5-turbo from OpenAI

# ---------- Step 1: API Key ----------
# Add your OpenAI API key here
KEY = "enter your key"

# ---------- Step 2: Web UI Layout ----------
# Streamlit header for the main app
st.header("Asmat Chatbot")

# Sidebar layout for file upload
with st.sidebar:
    st.title("Your Documents")
    doc = st.file_uploader("Upload your PDF File")

# ---------- Step 3: Process the Uploaded PDF ----------
if doc is not None:
    # Read the PDF
    pdf = PdfReader(doc)
    words = ""
    
    # Extract text from all pages
    for page in pdf.pages:
        words += page.extract_text()

    # ---------- Step 4: Text Splitting ----------
    # Split text into manageable chunks
    text_splitter = RecursiveCharacterTextSplitter(
        separators="\n",      # Split by newline
        chunk_size=1000,      # Max characters per chunk
        chunk_overlap=150,    # Overlap to preserve context
        length_function=len
    )
    portion = text_splitter.split_text(words)

    # ---------- Step 5: Embedding Creation ----------
    # Generate text embeddings using OpenAI
    embeddings = OpenAIEmbeddings(openai_api_key=KEY)

    # Create vector database with FAISS
    vector = FAISS.from_texts(portion, embeddings)

# ---------- Step 6: User Question Input ----------
# Ask user to input a question
question = st.text_input("Write your question")

# ---------- Step 7: Answer Generation ----------
if question:
    # Search for relevant text chunks using vector similarity
    match = vector.similarity_search(question)

    # Load OpenAI language model (chat)
    llm = ChatOpenAI(
        openai_api_key=KEY,
        temperature=0.2,        # Control randomness
        max_tokens=1000,        # Max tokens in response
        model_name='gpt-3.5-turbo'  # OpenAI model
    )
    
    # Load QA chain using the retrieved documents
    chain = load_qa_chain(llm, chain_type='stuff')

    # Generate answer using retrieved context and user's question
    response = chain.run(input_documents=match, question=question)

    # Display answer in Streamlit
    st.write(response)
