from langchain_community.embeddings.ollama import OllamaEmbeddings
from langchain_community.embeddings.bedrock import BedrockEmbeddings
from langchain_community.embeddings.openai import OpenAIEmbeddings
from langchain_community.embeddings.huggingface import HuggingFaceInferenceAPIEmbeddings
from langchain_community.embeddings.huggingface import HuggingFaceEmbeddings


# model = "Alibaba-NLP/gte-large-en-v1.5"
# model = "sentence-transformers/all-MiniLM-l6-v2"

# def get_embedding_function():
#     embeddings = HuggingFaceEmbeddings(model_name=model)
#     return embeddings

#----------------------------------------------------------------------------------------------------------------------
# def get_embedding_function():
#     embeddings = HuggingFaceEmbeddings(model_name="Salesforce/SFR-Embedding-Mistral")
#     return embeddings

#----------------------------------------------------------------------------------------------------------------------
# def get_embedding_function():
#     embeddings=OllamaEmbeddings(model="nomic-embed-text")
#     return embeddings


#----------------------------------------------------------------------------------------------------------------------
# def get_embedding_function():
#     embeddings=OllamaEmbeddings(model="mxbai-embed-large:latest")
#     return embeddings

#----------------------------------------------------------------------------------------------------------------------
# import dotenv
# import os

# dotenv.load_dotenv()
# inference_api_key=os.getenv("huggingface_api_key")

# def get_embedding_function():
#     embeddings = HuggingFaceInferenceAPIEmbeddings(
#         api_key=inference_api_key, model_name="sentence-transformers/all-MiniLM-l6-v2"
#     )
#     return embeddings
#----------------------------------------------------------------------------------------------------------------------
def get_embedding_function():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-l6-v2")
    return embeddings

#----------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    embeddings=get_embedding_function()
    text = "This is a test document."
    query_result = embeddings.embed_query(text)
    print(query_result[:3])
    
