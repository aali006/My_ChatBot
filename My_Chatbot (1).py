#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st 


# In[2]:


from PyPDF2 import PdfReader


# In[3]:


from langchain.text_splitter import RecursiveCharacterTextSplitter


# In[4]:


from langchain.vectorstores import FAISS


# In[5]:


from langchain.embeddings.openai import OpenAIEmbeddings


# In[6]:


from langchain.chains.question_answering import load_qa_chain


# In[7]:


from langchain.chat_models import ChatOpenAI


# In[8]:


# openai key


# In[9]:


KEY = "enter your key"


# In[10]:


# To upload PDF files


# In[11]:


st.header("Asmat Chatbot")


# In[12]:


with st.sidebar:
    st.title("Your Documents")
    doc = st.file_uploader("Upload your Pdf File")


# In[13]:


# Extract text


# In[14]:


if doc is not None:
    pdf = PdfReader(file)
    words = ""
    for page in pdf.pages:
        words += page.extract_text()

#Break it into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        separators="\n",
        chunk_size=1000,
        chunk_overlap=150,
        length_function=len
    )
    portion = text_splitter.split_text(words)


    # generating embedding
    embeddings = OpenAIEmbeddings(openai_api_key=KEY)

    # creating vector store - FAISS
    vector = FAISS.from_texts(portion, embeddings)


# In[15]:


# box to enter question


# In[16]:


question = st.text_input("write your question")


# In[17]:


# similarity test


# In[18]:


if question:
    match = vector.similarity_search(question)
    # llm
    llm = ChatOpenAI(
        openai_api_key = KEY,
        temperature = 0.2,
        max_tokens = 1000,
        model_name = 'gpt-3.5-turbo'     
    )
    
    #output
    chain = load_qa_chain(llm, chain_type = 'stuff')
    response = chain.run(input_documents = match, question = question)
    st.write(response)


# In[ ]:




