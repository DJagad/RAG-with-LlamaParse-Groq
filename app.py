import os
import requests
import streamlit as st
import nest_asyncio
import pickle
from dotenv import load_dotenv
from llama_index.vector_stores.qdrant import QdrantVectorStore
from llama_index.core import VectorStoreIndex, StorageContext
from qdrant_client import QdrantClient
from llama_index.embeddings.fastembed import FastEmbedEmbedding
from llama_index.core import Settings
from llama_index.llms.groq import Groq
from llama_parse import LlamaParse

# Load or parse the data
def load_or_parse_data():
    data_file = "./data/parsed_data.pkl"
    if os.path.exists(data_file):
        with open(data_file, "rb") as f:
            parsed_data = pickle.load(f)
    else:
        llamaparse_api_key = os.getenv('LLAMA_CLOUD_API_KEY')
        llama_parse_documents = LlamaParse(api_key=llamaparse_api_key, result_type="markdown").load_data(["./data/presentation.pptx", "./data/uber_10q_march_2022.pdf"])
        with open(data_file, "wb") as f:
            pickle.dump(llama_parse_documents, f)
        parsed_data = llama_parse_documents
    return parsed_data

# Load the Groq models dynamically
def load_groq_model(model_name, groq_api_key):
    return Groq(model=model_name, api_key=groq_api_key)

# Streamlit frontend
def main():

    load_dotenv()
    
    st.title("RAG Frontend")

    # Create the 'data' directory if it doesn't exist
    if not os.path.exists('data'):
        os.makedirs('data')

    # Download the first file
    url1 = 'https://raw.githubusercontent.com/run-llama/llama_index/main/docs/docs/examples/data/10q/uber_10q_march_2022.pdf'
    file_path1 = './data/uber_10q_march_2022.pdf'
    response1 = requests.get(url1)
    with open(file_path1, 'wb') as file:
        file.write(response1.content)

    # Download the second file
    url2 = 'https://meetings.wmo.int/Cg-19/PublishingImages/SitePages/FINAC-43/7%20-%20EC-77-Doc%205%20Financial%20Statements%20for%202022%20(FINAC).pptx'
    file_path2 = './data/presentation.pptx'
    response2 = requests.get(url2)
    with open(file_path2, 'wb') as file:
        file.write(response2.content)

    print('Files downloaded successfully!')

    # Set up the Qdrant vector store and the Groq LLM
    qdrant_url = os.getenv("QDRANT_URL")
    #print(qdrant_url)
    qdrant_api_key = os.getenv("QDRANT_API_KEY")
    #print(qdrant_api_key)
    groq_api_key = os.getenv("GROQ_API_KEY")
    print(groq_api_key)

    # Allow user to select a model
    model_options = ["mixtral-8x7b-32768", "gemma-7b-it", "llama2-70b-4096"]
    selected_model = st.selectbox("Select a model", model_options)

    query = st.text_input("Enter your query", "")
    #st.write("query:-",query)
    
    if st.button("Submit"):
        
        embed_model = FastEmbedEmbedding(model_name="BAAI/bge-base-en-v1.5")
        Settings.embed_model = embed_model
        
        llm = load_groq_model(selected_model, groq_api_key=groq_api_key)
        print("Selected Model:", selected_model)
        Settings.llm = llm
        llama_parse_documents = load_or_parse_data()

        #print(llama_parse_documents)

        client = QdrantClient(api_key=qdrant_api_key, url=qdrant_url)
        vector_store = QdrantVectorStore(client=client, collection_name='qdrant_url')
        storage_context = StorageContext.from_defaults(vector_store=vector_store)
        index = VectorStoreIndex.from_documents(documents=llama_parse_documents, storage_context=storage_context)
        query_engine = index.as_query_engine()

        #print(query_engine)

        if query:
            st.write(query)
            response = query_engine.query(query)
            #print(response)
            st.write(response.response)

if __name__ == "__main__":
    main()