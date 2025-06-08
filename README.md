# 📄 DocuChat: Conversational PDF Question Answering App

DocuChat is an intelligent PDF-based chatbot built with **LangChain**, **OpenAI**, and **Streamlit**. Just upload any PDF file (e.g., research paper, resume, contract), ask questions about it, and get direct answers — powered by GPT-3.5.

---

## 🔍 What it Does

✅ Upload any PDF document  
✅ Extracts and understands its contents  
✅ Asks questions like:  
- “Summarize this paper”  
- “What are the key findings?”  
- “What was the total expense in the invoice?”  

Answers are contextually generated from the PDF, not generic!

---

## ⚙️ Tech Stack

| Layer       | Technology                     |
|------------|---------------------------------|
| UI         | Streamlit                       |
| Backend    | Python, LangChain               |
| LLM        | OpenAI GPT-3.5-Turbo            |
| Embedding  | OpenAI Embeddings               |
| Vector DB  | FAISS                           |
| PDF Reader | PyPDF2                          |

---

## 📦 Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone [https://github.com/aali006/My_ChatBot.git]
cd docu-chatbot
```

###2. Add Your OpenAI API Key
KEY = "your-openai-key-here"

###3. Run the App

**How It Works**-
- User uploads a PDF using the sidebar.

- PDF text is extracted using PyPDF2.

- Text is split into chunks for semantic understanding.

- Each chunk is converted into vector embeddings using OpenAI Embeddings.

- FAISS vector database indexes and stores these chunks.

- When a question is asked:

- The app retrieves the most relevant chunks from FAISS.

- GPT-3.5-Turbo generates a final answer using those retrieved chunks.

  ![Asmat’s ChatBot](https://github.com/user-attachments/assets/0c660bb3-7990-43ac-909b-f43f18a6f57d)



