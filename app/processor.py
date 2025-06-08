from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings

OPENAI_API_KEY = "enter your key"

def process_pdf(doc):
    pdf = PdfReader(doc)
    words = ""

    for page in pdf.pages:
        words += page.extract_text()

    text_splitter = RecursiveCharacterTextSplitter(
        separators="\n",
        chunk_size=1000,
        chunk_overlap=150,
        length_function=len
    )

    portions = text_splitter.split_text(words)
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    vector_store = FAISS.from_texts(portions, embeddings)
    return vector_store
