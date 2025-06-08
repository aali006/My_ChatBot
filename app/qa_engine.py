from langchain.chains.question_answering import load_qa_chain
from langchain.chat_models import ChatOpenAI

OPENAI_API_KEY = "enter your key"

def get_answer(vector_store, question):
    matched_docs = vector_store.similarity_search(question)

    llm = ChatOpenAI(
        openai_api_key=OPENAI_API_KEY,
        temperature=0.2,
        max_tokens=1000,
        model_name='gpt-3.5-turbo'
    )

    chain = load_qa_chain(llm, chain_type='stuff')
    response = chain.run(input_documents=matched_docs, question=question)
    return response
