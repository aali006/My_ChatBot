import streamlit as st
from app.processor import process_pdf
from app.qa_engine import get_answer

def launch_pdf_chatbot():
    st.set_page_config(page_title="PDF Q&A Chatbot", layout="centered")
    st.header("Asmat Chatbot")

    with st.sidebar:
        st.title("Your Documents")
        doc = st.file_uploader("Upload your PDF File")

    vector_store = None
    if doc is not None:
        vector_store = process_pdf(doc)

    question = st.text_input("Write your question")

    if question and vector_store:
        response = get_answer(vector_store, question)
        st.subheader("Answer")
        st.write(response)
